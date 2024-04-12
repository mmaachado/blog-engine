from blog.models import Post, Page
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import Http404

PER_PAGE: int = 9


def index(request):
    posts = Post.objects.get_published()
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': '~/ ',
        },
    )


def category(request, slug):
    posts = Post.objects.get_published().filter(category__slug=slug)
    
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if len(page_obj) == 0:
        raise Http404()
    
    page_title = f'{page_obj[0].category.name} - '

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title,
        },
    )


def tag(request, slug):
    posts = Post.objects.get_published().filter(tags__slug=slug)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404()

    page_title = f'#{page_obj[0].tags.first().name} - '

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title,
        }
    )


def search(request):
    search_value = request.GET.get('search', '')

    posts = Post.objects.get_published().filter(
        Q(title__icontains=search_value) |
        Q(excerpt__icontains=search_value) |
        Q(content__icontains=search_value)
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

    page_object = Page.objects.filter(is_published=True).filter(slug=slug).first()

    if page_object is None:
        raise Http404()

    page_title = page_object.title

    return render(
        request,
        'blog/pages/page.html',
        {
            'page': page_object,
            'page_title': page_title,
        })


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


def created_by(request, author_pk):
    user = User.objects.filter(pk=author_pk).first()

    if user is None:
        raise Http404()

    posts = Post.objects.get_published().filter(created_by__pk=author_pk)
    user_full_name = user.username

    if user.first_name:
        user_full_name = f'{user.first_name} {user.last_name}'

    page_title = user_full_name + ' posts - '

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title,
        },
    )