# -*- coding: utf-8 -*-

import requests
from .models import Location

def getLocation(ip):

    #Hacemos una petición HTTP
    url = "http://ip-api.com/json/" + ip
    r = requests.get(url)
    aux = r.json()
    print( "============================================================ " )
    print( aux.get("status"))

    if aux.get("status") == "success":
        #Creamos un objeto Location con el resultado
        l = Location()
        l.ip = ip
        l.timezone = aux.get("timezone", "")
        l.countryCode = aux.get("countryCode", "")
        l.org = aux.get("org", "")
        l.region = aux.get("region", "")
        l.latitud = aux.get("lat", "")
        l.longitud = aux.get("lon", "")
        l.country = aux.get("country", "")
        l.regionName = aux.get("regionName", "")
        l.isp = aux.get("isp", "")
        l.city = aux.get("city", "")
        l.save()
        return l;
    else :
          return None

def getOS(user_agent):
    url = "http://helloacm.com/api/parse-user-agent/?s=nUser-Agent:" + user_agent
    r = requests.get(url)
    print( r.json() )

def getVendor(mac):
    url = "http://api.macvendors.com/" + mac
    r = requests.get(url)
    print("====================================")
    print(r.text)