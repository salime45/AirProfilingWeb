from django.conf.urls import url
from .views import index
from .views import getProfiles

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^profiles/$', getProfiles, name='profiles'),
]