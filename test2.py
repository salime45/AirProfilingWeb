
import os
import django


#configuramos django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "air_profiling.settings")
django.setup()

from django.db.models import Q

from core.models import Link
from core.models import Perfil
from updater.models import Pcap

def test():
        perfil = '10:fe:ed:f5:01:fc'
        auxp = Perfil.objects.get(pk=perfil)
        pcaps_ids = Link.objects.filter(Q(perfil_dst=auxp) | Q(perfil_src=auxp)).values('pcap').distinct()
        print("--->" + str( len(pcaps_ids) ))
        print("--->" + str( pcaps_ids) )
        pcaps= []
        for p in  pcaps_ids:
            auxp = Pcap.objects.get(pk=p.get('pcap'))
            pcaps.append(auxp)

        print("--->" + str( pcaps) )



test()



