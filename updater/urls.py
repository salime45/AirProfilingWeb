from django.conf.urls import url
from .views import getPcap
from .views import updatePcap
from .jsons import getPcaps
from .jsons import getDetailsPcap

urlpatterns = [
    url(r'^pcaps/$', getPcaps, name='pcaps'),
    url(r'^pcap$', getPcap, name='pcap'),
    url(r'^update', updatePcap, name='update'),
    url(r'^detailsPcap$', getDetailsPcap, name='detailsPcap'),
]