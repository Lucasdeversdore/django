from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from monApp.models import Categorie, Produit, Statut, Rayon, Contenir
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from monApp.forms import ContactUsForm, ProduitForm, CategorieForm, RayonForm
from django.shortcuts import redirect
from django.forms import BaseModelForm
from django.urls import reverse_lazy
from django.db.models import Count, Prefetch
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# def home(request,param=None):
#     print (dir(request))
#     if param is None:
#         return HttpResponse("<h1>Hello Django!</h1>")
#     else:
#         return HttpResponse(f"<h1>Hello {param} !</h1>")
#     if request.GET and request.GET['name']:
#         string = request.GET["name"]
#         return HttpResponse("<h1>Hello %s </h1>" % string)
#     elif param is None:
#         return HttpResponse("<h1>Hello Django!</h1>")
#     else : 
#         return HttpResponse(f"<h1>Hello {param} !</h1>")

# def accueil(request,param=None):
#     if request.GET and request.GET['name']:
#         string = request.GET["name"]
#         return render(request, 'monApp/home.html',{'param': string})
#     return render(request, 'monApp/home.html',{'param': param})

# def contact(request):
#     return render(request, 'monApp/contactus.html')

# def about(request):
#     return render(request, 'monApp/aboutus.html')

# def ListProduits(request):
#     prdts = Produit.objects.all()
#     return render(request, 'monApp/list_produits.html',{'prdts': prdts})

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

class HomeView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        param = self.kwargs.get('param')
        context['titreh1'] = f"Hello {param}" if param else "Hello Django"
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)
        

class AboutView(TemplateView):
    template_name = "monApp/page_home.html"
    
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us..."
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)

def ContactView(request):
    titreh1 = "Contact us !"
    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject = f'Message from {form.cleaned_data["name"] or "anonyme"} via MonProjet Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@monprojet.com'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, "monApp/page_home.html",{'titreh1':titreh1, 'form':form})

class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"
    
    def get_queryset(self):
        # Charge les catégories et les statuts en même temps
        return Produit.objects.select_related('categorie').select_related('statutProd')

    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context
class EmailSentView(TemplateView):
    template_name = "monApp/email_sent.html"
    
class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"

    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context

class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "categories" 

    def get_queryset(self):
    # Annoter chaque catégorie avec le nombre de produits liés
        return Categorie.objects.annotate(nb_produits=Count('produits'))
    
    def get_context_data(self, **kwargs):
        context = super(CategorieListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes catégories"
        return context

class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "cate"

    def get_queryset(self):
    # Annoter chaque catégorie avec le nombre de produits liés
        return Categorie.objects.annotate(nb_produits=Count('produits'))
    
    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        context['prdts'] = self.object.produits.all()
        return context


class StatutListView(ListView):
    model = Statut
    template_name = "monApp/list_statuts.html"
    context_object_name = "statuts" 

    def get_context_data(self, **kwargs):
        context = super(StatutListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des statuts"
        return context

class StatutDetailView(DetailView):
    model = Statut
    template_name = "monApp/detail_statut.html"
    context_object_name = "stat"

    def get_context_data(self, **kwargs):
        context = super(StatutDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du statut"
        return context

class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rayons" 

    def get_queryset(self):
        # Précharge tous les "contenir" de chaque rayon,
        # et en même temps le produit de chaque contenir
        return Rayon.objects.prefetch_related(
            Prefetch("contenirR", queryset=Contenir.objects.select_related("refProd"))
        )

    def get_context_data(self, **kwargs):
        context = super(RayonListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des rayons"
        ryns_dt = []
        for rayon in context['rayons']:
            total = 0
            for contenir in rayon.contenirR.all():
                total += contenir.refProd.prixUnitaireProd * contenir.qte
            ryns_dt.append({
                'rayon': rayon,
                'total_stock': total
            })
        context['ryns_dt'] = ryns_dt
        return context



class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "ray"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"

        prdts_dt = []
        total_rayon = 0
        total_nb_produit = 0

        for contenir in self.object.contenirR.all():
            total_produit = contenir.refProd.prixUnitaireProd * contenir.qte
            prdts_dt.append({
                'produit': contenir.refProd,
                'qte': contenir.qte,
                'prix_unitaire': contenir.refProd.prixUnitaireProd,
                'total_produit': total_produit
            })
            total_rayon += total_produit
            total_nb_produit += contenir.qte

        context['prdts_dt'] = prdts_dt
        context['total_rayon'] = total_rayon
        context['total_nb_produit'] = total_nb_produit
        return context



class ConnectView(LoginView):
    template_name = 'monApp/page_login.html'
    def post(self, request, **kwargs):
        lgn = request.POST.get('username', False)
        pswrd = request.POST.get('password', False)
        user = authenticate(username=lgn, password=pswrd)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'monApp/page_home.html', {'param': lgn, 'message': "You're connected"})
        else:
            return render(request, 'monApp/page_register.html')


class RegisterView(TemplateView):
    template_name = 'monApp/page_register.html'
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'monApp/page_login.html')
        else:
            return render(request, 'monApp/page_register.html')

class DisconnectView(TemplateView):
    template_name = 'monApp/page_logout.html'
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)

@method_decorator(login_required, name='dispatch')
class ProduitCreateView(CreateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/create_produit.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)

@method_decorator(login_required, name='dispatch')
class ProduitUpdateView(UpdateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/update_produit.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)

@method_decorator(login_required, name='dispatch')
class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = "monApp/delete_produit.html"
    success_url = reverse_lazy('lst_prdts')

@method_decorator(login_required, name='dispatch')
class CategorieCreateView(CreateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/create_categorie.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        cate = form.save()
        return redirect('dtl_cate', cate.idCat)
@method_decorator(login_required, name='dispatch')
class CategorieUpdateView(UpdateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/update_categorie.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        cate = form.save()
        return redirect('dtl_cate', cate.idCat)
@method_decorator(login_required, name='dispatch')
class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "monApp/delete_categorie.html"
    success_url = reverse_lazy('lst_cate')
@method_decorator(login_required, name='dispatch')
class RayonCreateView(CreateView):
    model = Rayon
    form_class=RayonForm
    template_name = "monApp/create_rayon.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        rayon = form.save()
        return redirect('dtl_rayon', rayon.idRayon)
@method_decorator(login_required, name='dispatch')
class RayonUpdateView(UpdateView):
    model = Rayon
    form_class=RayonForm
    template_name = "monApp/update_rayon.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        rayon = form.save()
        return redirect('dtl_rayon', rayon.idRayon)
@method_decorator(login_required, name='dispatch')
class RayonDeleteView(DeleteView):
    model = Rayon
    template_name = "monApp/delete_rayon.html"
    success_url = reverse_lazy('lst_rayon')

# def ProduitUpdate(request, pk):
#     prdt = Produit.objects.get(refProd=pk)
#         if request.method == 'POST':
#             form = ProduitForm(request.POST, instance=prdt)
#             if form.is_valid():
#                 # mettre à jour le produit existant dans la base de données
#                 form.save()
#                 # rediriger vers la page détaillée du produit que nous venons de mettre à jour
#                 return redirect('dtl-prdt', prdt.refProd)
#         else:
#             form = ProduitForm(instance=prdt)
#         return render(request,'monApp/update_produit.html', {'form': form})