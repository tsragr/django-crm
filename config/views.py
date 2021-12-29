from django.views import generic


class IndexView(generic.TemplateView):
    """
    Start service's page
    """
    template_name = 'base.html'
