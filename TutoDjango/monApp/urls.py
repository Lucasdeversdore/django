from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
#path("home/", views.home, name="home"),
path("about/", views.AboutView.as_view()),
path("contact/", views.contact, name="contact"),
path('home/<param>',views.accueil ,name='accueil'),
path('produits/',views.ListProduits ,name='produits'),
path('categories/',views.ListCategorie ,name='categories'),
path('statuts/',views.ListStatut,name='statuts'),
path('rayons/',views.ListRayon,name='rayons'),
path("home/", views.HomeView.as_view()),
]