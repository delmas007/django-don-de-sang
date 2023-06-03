from django.urls import path
from base.views import inscription,Connexion,Deconnexion,HopitalR,Demande,Administrateur,bienvenue

app_name = 'base'

urlpatterns = [
    path('Inscription/', inscription,name = 'inscription'),
    path('Connexion/', Connexion.as_view(),name = 'connexion'),
    path('Deconnexion/', Deconnexion.as_view(),name = 'Deconnexion'),
    # path('Deconnexion/', Deconnexion.as_view(),name = 'Deconnexion'),
    path('Disponibilité du sang/', HopitalR,name = 'hopital'),
    path('Demande de sang/', Demande,name = 'demande'),
    path('edite/<str:slug>/', Administrateur.as_view(),name = 'administrateur'),
    path('bienvenue/', bienvenue,name = 'bienvenue'),
]