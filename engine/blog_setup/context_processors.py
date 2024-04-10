from blog_setup.models import BlogSetup


def blog_setup(request):

    setup = BlogSetup.objects.order_by('-id').first()

    return {
        'blog_setup': setup,
    }
