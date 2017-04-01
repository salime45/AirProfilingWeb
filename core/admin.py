from django.contrib import admin
from .models import Perfil, Link, Location, Vendor, Dns, UserAgent


admin.site.register(Perfil)
admin.site.register(Link)
admin.site.register(Location)
admin.site.register(Vendor)
admin.site.register(Dns)
admin.site.register(UserAgent)
