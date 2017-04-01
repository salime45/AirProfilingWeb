
import os
import django
from user_agents import parse

#configuramos django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "air_profiling.settings")
django.setup()


from core.models import Link

def test():
    print("ñññññññññññ")
    links = Link.objects.exclude(user_agent = '').exclude(user_agent = None)

    for i in range(len(links)):

        s = parse(links[i].user_agent)
        print ("+"+  str(links[i].user_agent))
        print ("+"+  str(s))
        agent = str(s).split("/")
        print ("+"+  agent[0])
        print ("+"+  agent[1])
        print ("+"+  agent[2])

        print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


test()



