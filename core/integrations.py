# -*- coding: utf-8 -*-

import requests
import re
import socket

from user_agents import parse

from .models import Location
from .models import Vendor
from .models import UserAgent
from .models import Dns

import tacyt.TacytApp as tacytapp

def getLocation(ip, pcap):

    if not is_ip_private(ip):
        #Hacemos una petición HTTP
        url = "http://ip-api.com/json/" + ip
        print("Localizando ip " + ip)
        r = requests.get(url)
        aux = r.json()

        if aux.get("status") == "success":
            #Creamos un objeto Location con el resultado
            l = Location()
            l.pcap = pcap
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

def getHost(ip):

    dns = Dns.objects.filter(ip=ip);
    if not is_ip_private(ip) and len(dns) < 1:
        try:

            dns = Dns()
            host = socket.gethostbyaddr(ip)
            dns.ip = ip
            print(host)
            dns.host = host[0]
            dns.save()
            print("Obtenido host " + host[0] + " desde la ip : " +ip)
        except socket.error:
            print("Error obteniendo la ip : " + ip)

def getTacytApps(host):

    api = tacytapp.TacytApp("PpQbU3AWa773ghLdf2YE", "9UWa3aqaJKrqTkYqtbyUUmyP8uT39NmUYH4HuQWJ")
    result_search = api.search_apps("links:\"http://" + host + "\"",1 , 15, '' ,True)
    list = result_search.data.get('result').get('applications')

    return list

def getUA(user_agent):
    u = UserAgent.objects.filter(value = user_agent).first()

    if u is None:
        s = parse(user_agent)
        agent = str(s).split("/")
        u = UserAgent()
        u.value = user_agent
        u.os = agent[1]
        u.browser = agent[2]
        u.device = agent[0]
        u.save()


def getVendor(mac):
    print("Procesando " + mac)
    vendor = Vendor.objects.filter(mac=mac[0:8]).first()

    if vendor is None:
        print("Obteniendo fabricante para la MAC " + mac)
        url = "http://api.macvendors.com/" + mac
        r = requests.get(url)
        vendor = Vendor()
        vendor.mac=mac[0:8]
        vendor.fabricante=r.text
        vendor.save()
    return vendor

def is_ip_private(ip):

    # https://en.wikipedia.org/wiki/Private_network
    priv_lo = re.compile("^127\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    priv_24 = re.compile("^10\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    priv_20 = re.compile("^192\.168\.\d{1,3}.\d{1,3}$")
    priv_16 = re.compile("^172.(1[6-9]|2[0-9]|3[0-1]).[0-9]{1,3}.[0-9]{1,3}$")

    return priv_lo.match(ip) or priv_24.match(ip) or priv_20.match(ip) or priv_16.match(ip)



def isValidIP(ip):
    return not ip.startswith("192.168")

