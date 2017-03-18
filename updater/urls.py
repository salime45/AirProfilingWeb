from django.conf.urls import url
from .views import getPcaps

urlpatterns = [
    url(r'^pcaps/$', getPcaps, name='pcaps'),
]