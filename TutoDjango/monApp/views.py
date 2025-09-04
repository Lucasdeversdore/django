from django.shortcuts import render
from django.http import HttpResponse

from monApp.models import Categorie, Produit, Statut


def home2(request):
        return HttpResponse("<h1>Hello DJANGO")

def home(request, param):
    return HttpResponse("<h1>Hello " + param + "</h1>")

def contact(request):
    return HttpResponse("<h1>Contact us</h1>")

def about(request):
    return HttpResponse("<h1>About us</h1>")

def produit(request):
    lesProds = ListProduits()
    liste = "<ul>"
    for prod in lesProds:
        liste += f"<li> {prod.intituleProd} </li>"
    liste += "</ul>"
    return HttpResponse(liste)


def ListProduits():
    prdts = Produit.objects.all()
    return prdts

def categorie(request):
    lesCat = ListCategorie()
    liste = "<ul>"
    for cat in lesCat:
        liste += f"<li> {cat.nomCat} </li>"
    liste += "</ul>"
    return HttpResponse(liste)


def ListCategorie():
    prdts = Categorie.objects.all()
    return prdts


def statut(request):
    lesStatuts = ListStatut()
    liste = "<ul>"
    for statut in lesStatuts:
        liste += f"<li> {statut.libelleStatut} </li>"
    liste += "</ul>"
    return HttpResponse(liste)


def ListStatut():
    prdts = Statut.objects.all()
    return prdts