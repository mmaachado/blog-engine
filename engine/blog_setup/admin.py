from blog_setup.models import BlogSetup, MenuLink
from django.contrib import admin

# @admin.register(MenuLink)
# class MenuLinkAdmin(admin.ModelAdmin):
#     list_display = 'id', 'text', 'url_or_path',
#     list_display_links = 'id', 'text', 'url_or_path',
#     search_fields = 'id', 'text', 'url_or_path',


class MenuLinkInline(admin.TabularInline):
    model = MenuLink
    extra = 1


@admin.register(BlogSetup)
class BlogSetupAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
    )
    inlines = (MenuLinkInline,)

    def has_add_permission(self, request):
        return not BlogSetup.objects.exists()
