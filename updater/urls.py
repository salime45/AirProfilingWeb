from django.conf.urls import url
from .views import getPcaps
from .views import getPcap

urlpatterns = [
    url(r'^pcaps/$', getPcaps, name='pcaps'),
    url(r'^pcap$', getPcap, name='pcap'),]