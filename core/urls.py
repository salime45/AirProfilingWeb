from django.conf.urls import url
from .views import index
from .views import getPerfil
from .jsons import getDetailsPerfil
from .jsons import getProfiles

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^profiles/$', getProfiles, name='profiles'),
    url(r'^perfilDetails$', getDetailsPerfil, name='perfilDetails'),
    url(r'^perfil/$', getPerfil, name='perfil'),


]