
import os
import django


#configuramos django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "air_profiling.settings")
django.setup()

from core.models import Link
from core.models import Perfil
from updater.models import Pcap

def test():
        perfil = '90:68:c3:2e:96:53'
        auxp = Perfil.objects.get(pk=perfil)
        print("--->" + str( perfil) )

        user_agents = Link.objects.filter(perfil_src=auxp).exclude(user_agent='').values('user_agent').distinct()
        print("--->" + str( len(user_agents) ))

        for p in  user_agents:
            print(p)




test()



