from django.contrib import admin

# Register your models here.
from base.models import SiteDeDon,Commune,Hopital,Membre

@admin.register(SiteDeDon)
class Site(admin.ModelAdmin):
    pass

@admin.register(Commune)
class commune(admin.ModelAdmin):
    pass

@admin.register(Hopital)
class hopital(admin.ModelAdmin):
    list_display = ('nom', 'commune', 'id', 'Aplus',"slug")
    
@admin.register(Membre)
class Membre(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'contact',"groupe", 'is_active',"commune")