from django.conf.urls import url
from .views import index
from .views import perfil
from .views import timeline
from .views import apps
from .jsons import getDetailsPerfil
from .jsons import getProfiles
from .jsons import getUserAgents
from .jsons import getLinks
from .jsons import getApps

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^perfil/$', perfil, name='perfil'),
    url(r'^timeline/$', timeline, name='timeline'),
    url(r'^apps/$', apps, name='apps'),
    url(r'^getapps/$', getApps, name='getapps'),
    url(r'^profiles/$', getProfiles, name='profiles'),
    url(r'^links/$', getLinks, name='links'),
    url(r'^perfilDetails$', getDetailsPerfil, name='perfilDetails'),
    url(r'^agents', getUserAgents, name='agents'),


]