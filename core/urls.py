from django.conf.urls import url
from .views import index
from .views import perfil
from .views import timeline
from .jsons import getDetailsPerfil
from .jsons import getProfiles

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^perfil/$', perfil, name='perfil'),
    url(r'^timeline/$', timeline, name='timeline'),
    url(r'^profiles/$', getProfiles, name='profiles'),
    url(r'^perfilDetails$', getDetailsPerfil, name='perfilDetails'),


]