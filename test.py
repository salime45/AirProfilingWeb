
import os
import django
import socket


#configuramos django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "air_profiling.settings")
django.setup()

import tacyt.TacytApp as tacytapp
from core.models import Link

def testTacyct():

    api = tacytapp.TacytApp("PpQbU3AWa773ghLdf2YE", "9UWa3aqaJKrqTkYqtbyUUmyP8uT39NmUYH4HuQWJ")
    links = Link.objects.exclude(host='').values('host').distinct()
    for j in range(len(links)):

        host = links[j].get('host');
        host = host[2:len(host)-1]
        result_search = api.search_apps("links:\"http://" + host + "\"",1 , 100, '' ,True)
        list = result_search.data.get('result').get('applications')

        print("** " + host + " **")

        for i in range(len(list)):
            app = list[i]
            print (app.get('title'))

        print("\n\n==================================================================================\n\n")

def testDns():
    host = socket.gethostbyaddr("54.83.61.168")
    print("----- " + str(host[0]) )



testDns()



