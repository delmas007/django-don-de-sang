from django.urls import path
from affiche.views import pourquoi,information,test,site,reussite
from django.contrib.auth.decorators import login_required

app_name = 'affiche'

urlpatterns = [
    path('information sur le don/', information,name = 'information'),
    path('pourquoi faire un don/', pourquoi,name = 'pourquoi'),
    path('test/', login_required(test),name = 'test'),
    path('lieux de don/', site,name = 'site'),
    path('test/reusssit',login_required(reussite) ,name = 'reussite'),
]