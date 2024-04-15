from typing import Any

from blog.models import Page, Post
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic import ListView

PER_PAGE: int = 9


class PostListView(ListView):
    template_name = 'blog/pages/index.html'
    context_object_name = 'posts'
    paginate_by = PER_PAGE
    queryset = Post.objects.get_published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({'page_title': '~/'})

        return context


class CreatedByListView(PostListView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._temp_context: dict[str, Any] = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self._temp_context['user']
        user_full_name = user.username

        if user.first_name:
            user_full_name = f'{user.first_name} {user.last_name}'
        page_title = user_full_name + ' posts - '

        context.update(
            {
                'page_title': page_title,
            }
        )

        return context

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        queryset = queryset.filter(
            created_by__pk=self._temp_context['user'].pk
        )
        return queryset

    def get(self, request, *args, **kwargs):
        author_pk = self.kwargs.get('author_pk')
        user = User.objects.filter(pk=author_pk).first()

        if user is None:
            raise Http404()

        self._temp_context.update(
            {
                'author_pk': author_pk,
                'user': user,
            }
        )

        return super().get(request, *args, **kwargs)


class CategoryListView(PostListView):
    allow_empty = False

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(category__slug=self.kwargs.get('slug'))
        )

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        page_title = f'{self.object_list[0].category.name}'
        context.update(
            {
                'page_title': page_title,
            }
        )
        return context


class TagListView(PostListView):
    allow_empty = False

    def get_queryset(self):
        return (
            super().get_queryset().filter(tags__slug=self.kwargs.get('slug'))
        )

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        page_title = f'#{self.object_list[0].tags.first().name}'
        context.update(
            {
                'page_title': page_title,
            }
        )
        return context


class SearchListView(PostListView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._search_value = ''

    def setup(self, request, *args, **kwargs):
        self._search_value = request.GET.get('search', '').strip()
        return super().setup(request, *args, **kwargs)

    def get_queryset(self) -> QuerySet[Any]:
        return (
            super()
            .get_queryset()
            .filter(
                Q(title__icontains=self._search_value)
                | Q(excerpt__icontains=self._search_value)
                | Q(content__icontains=self._search_value)
            )[:PER_PAGE]
        )

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'page_title': f'cat {self._search_value[:30]}',
                'search_value': self._search_value,
            }
        )

        return context

    def get(self, request, *args, **kwargs):
        if self._search_value == '':
            return redirect('blog:index')
        return super().get(request, *args, **kwargs)


def search(request):
    search_value = request.GET.get('search', '')

    posts = Post.objects.get_published().filter(
        Q(title__icontains=search_value)
        | Q(excerpt__icontains=search_value)
        | Q(content__icontains=search_value)
    )[:PER_PAGE]

    if len(posts) == 0:
        raise Http404()

    page_title = f'cat {search_value[:30]} - '

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': posts,
            'search_value': search_value,
            'page_title': page_title,
        },
    )


def page(request, slug):

    page_object = (
        Page.objects.filter(is_published=True).filter(slug=slug).first()
    )

    if page_object is None:
        raise Http404()

    page_title = page_object.title

    return render(
        request,
        'blog/pages/page.html',
        {
            'page': page_object,
            'page_title': page_title,
        },
    )


def post(request, slug):
    post_object = Post.objects.get_published().filter(slug=slug).first()

    if post_object is None:
        raise Http404()

    post_title = post_object.title

    return render(
        request,
        'blog/pages/post.html',
        {
            'post': post_object,
            'page_title': post_title,
        },
    )
