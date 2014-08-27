from django.conf.urls import url

from distributor import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    #~ url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #~ url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    #~ url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

#~ from django.conf.urls.defaults import *
#~ from django.views import generic
#~ from polls.models import Question, Choice

#~ from mysite.books.models import Publisher

#~ publisher_info = {
    #~ 'queryset': Choice.objects.all(),
#~ }

#~ urlpatterns = [url(r'^publishers/$',  generic.list.ListView, publisher_info)]
