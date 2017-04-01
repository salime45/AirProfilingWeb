
import os
import django
import httpagentparser

#configuramos django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "air_profiling.settings")
django.setup()


from core.models import Link

def test():
    print("ñññññññññññ")
    links = Link.objects.exclude(user_agent = '').exclude(user_agent = None)

    for i in range(len(links)):

        if links[i] != None and links[i].user_agent !=  'None':
            s = httpagentparser.detect(links[i].user_agent)
            if s != 'None' :
                print ("+"+  str(s))
                print ("+"+  str(s.get('platform')))
                print ("+"+  str(s.get('platform').get('name') + " "+ s.get('platform').get('version')  ))
                print ("+"+  str(s.get('browser').get('name') + " "+ s.get('browser').get('version')  ))
                print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


test()



