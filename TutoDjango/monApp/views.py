from django.shortcuts import render
from django.http import HttpResponse

from monApp.models import Categorie, Produit, Statut, Rayon


def home(request,param=None):
    print (dir(request))
    if param is None:
        return HttpResponse("<h1>Hello Django!</h1>")
    else:
        return HttpResponse(f"<h1>Hello {param} !</h1>")
    if request.GET and request.GET['name']:
        string = request.GET["name"]
        return HttpResponse("<h1>Hello %s </h1>" % string)
    elif param is None:
        return HttpResponse("<h1>Hello Django!</h1>")
    else : 
        return HttpResponse(f"<h1>Hello {param} !</h1>")

def accueil(request,param=None):
    if request.GET and request.GET['name']:
        string = request.GET["name"]
        return render(request, 'monApp/home.html',{'param': string})
    return render(request, 'monApp/home.html',{'param': param})

def contact(request):
    return render(request, 'monApp/contactus.html')

def about(request):
    return render(request, 'monApp/aboutus.html')

def ListProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html',{'prdts': prdts})

def categorie(request):
    lesCat = ListCategorie()
    liste = "<ul>"
    for cat in lesCat:
        liste += f"<li> {cat.nomCat} </li>"
    liste += "</ul>"
    return HttpResponse(liste)


def ListCategorie(request):
    categories = Categorie.objects.all()
    return render(request, 'monApp/list_categories.html',{'categories': categories})

def ListStatut(request):
    statuts = Statut.objects.all()
    return render(request, 'monApp/list_statuts.html',{'statuts': statuts})

def ListRayon(request):
    rayons = Rayon.objects.all()
    return render(request, 'monApp/list_rayons.html',{'rayons': rayons})