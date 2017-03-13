from django.conf.urls import url
from .views import index
from .views import getPcaps
from .views import getProfiles

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^pcaps/$', getPcaps, name='pcaps'),
    url(r'^profiles/$', getProfiles, name='profiles'),
]