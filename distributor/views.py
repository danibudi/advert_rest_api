from django.views import generic
class IndexView(generic.ListView):
    template_name = 'distributor/index.html'
