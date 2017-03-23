from django.conf.urls import url
from .views import index
from .jsons import getProfiles

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^profiles/$', getProfiles, name='profiles'),
]