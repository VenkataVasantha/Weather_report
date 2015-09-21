from django.conf.urls import url
from . import views



urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<zipcode>[0-9]+)/$', views.results, name='results'),
]
	