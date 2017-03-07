from django.conf.urls import url
from .views import list
from .views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^list/$', list, name='list'),
]