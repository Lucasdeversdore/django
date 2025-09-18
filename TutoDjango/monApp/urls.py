from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
#path("home/", views.home, name="home"),
path("about/", views.AboutView.as_view()),
path("contact/", views.ContactView.as_view()),
path('home/<param>',views.HomeView.as_view()),
path("produits/",views.ProduitListView.as_view(),name="lst_prdts"),
path('categories/',views.CategorieListView.as_view() ,name='lst_cate'),
path('statuts/',views.StatutListView.as_view() ,name='lst_stat'),
path('rayons/',views.RayonListView.as_view() ,name='lst_rayon'),
path("home/", views.HomeView.as_view()),
path("produit/<pk>/" ,views.ProduitDetailView.as_view(), name="dtl_prdt"),
path("categories/<pk>/" ,views.CategorieDetailView.as_view(), name="dtl_cate"),
path("statuts/<pk>/" ,views.StatutDetailView.as_view(), name="dtl_stat"),
path("rayons/<pk>/" ,views.RayonDetailView.as_view(), name="dtl_rayon"),
]