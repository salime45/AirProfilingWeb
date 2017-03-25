from django.conf.urls import url
from .views import index
from .views import getPerfilDetails
from .jsons import getProfiles

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^profiles/$', getProfiles, name='profiles'),
    url(r'^perfil/$', getPerfilDetails, name='perfil'),

]