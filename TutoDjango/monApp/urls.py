from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
#path("home/", views.home, name="home"),
path("about/", views.AboutView.as_view()),
path("contact/", views.ContactView, name="contact"),
path('home/<param>',views.HomeView.as_view()),
path("home/", views.HomeView.as_view(), name="home"),
path("produits/",views.ProduitListView.as_view(),name="lst_prdts"),
path('categoriess/',views.CategorieListView.as_view() ,name='lst_cate'),
path('statuts/',views.StatutListView.as_view() ,name='lst_stat'),
path('rayonss/',views.RayonListView.as_view() ,name='lst_rayon'),
path("home/", views.HomeView.as_view()),
path("produit/<pk>/" ,views.ProduitDetailView.as_view(), name="dtl_prdt"),
path("categories/<pk>/" ,views.CategorieDetailView.as_view(), name="dtl_cate"),
path("statuts/<pk>/" ,views.StatutDetailView.as_view(), name="dtl_stat"),
path("rayons/<pk>/" ,views.RayonDetailView.as_view(), name="dtl_rayon"),
path('login/', views.ConnectView.as_view(), name='login'),
path('register/', views.RegisterView.as_view(), name='register'),
path('logout/', views.DisconnectView.as_view(), name='logout'),
path('email-sent/', views.EmailSentView.as_view(), name='email-sent'),
path("produit/",views.ProduitCreateView.as_view(), name="crt-prdt"),
path("produit/<pk>/update/",views.ProduitUpdateView.as_view(), name="prdt-chng"),
path("produit/<pk>/delete/",views.ProduitDeleteView.as_view(), name="dlt-prdt"),
path("categories/",views.CategorieCreateView.as_view(), name="crt-cate"),
path("rayons/",views.RayonCreateView.as_view(), name="crt-rayon"),
path("rayons/<pk>/update/",views.RayonUpdateView.as_view(), name="rayon-chng"),
path("categories/<pk>/update/",views.CategorieUpdateView.as_view(), name="cate-chng"),
path("rayons/<pk>/delete/",views.RayonDeleteView.as_view(), name="dlt-rayon"),
path("categories/<pk>/delete/",views.CategorieDeleteView.as_view(), name="dlt-cate"),
]