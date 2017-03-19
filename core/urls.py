from django.conf.urls import url
from .views import index
from .views import updatePcap
from .views import getProfiles

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^update', updatePcap, name='update'),
    url(r'^profiles/$', getProfiles, name='profiles'),
]