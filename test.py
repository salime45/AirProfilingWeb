
import os
import django


#configuramos django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "air_profiling.settings")
django.setup()

from core.models import Link
from core.integrations import getHost

def test():

        lista = Link.objects.filter(host='')



        for l in  lista:
            getHost(l.ip_src)
            getHost(l.ip_dst)



test()



