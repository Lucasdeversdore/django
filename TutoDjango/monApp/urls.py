from django.urls import path
from . import views

urlpatterns = [
path('home/',views.home2, name='home'),
path('home/<param>',views.home, name='home'),
path("contact/", views.contact, name="contact"),
path("about/", views.about, name="about"),
path("produit/", views.produit, name="produit"),
path("categorie/", views.categorie, name="categorie"),
path("statut/", views.statut, name="statut"),
]