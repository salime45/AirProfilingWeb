
import os
import django


#configuramos django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "air_profiling.settings")
django.setup()

import tacyt.tacyt.TacytApp as tacytapp

def test():

    api = tacytapp.TacytApp("PpQbU3AWa773ghLdf2YE", "9UWa3aqaJKrqTkYqtbyUUmyP8uT39NmUYH4HuQWJ")
    result_search = api.search_apps("links:\"http://www.emtvalencia.es\"",1 , 100, '' ,True)

    list = result_search.data.get('result').get('applications')

    for i in range(len(list)):
        app = list[i]
        print (app.get('title'))

test()



