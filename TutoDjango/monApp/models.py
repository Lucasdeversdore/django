from django.db import models
from django.core.exceptions import ValidationError

class Categorie(models.Model):

    idCat = models.AutoField(primary_key=True)
    nomCat = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nomCat

class Statut(models.Model):

    idStatut = models.AutoField(primary_key=True)
    libelleStatut = models.CharField(max_length=150)

    def __str__(self):
        return self.libelleStatut
    
class Produit(models.Model):
    refProd = models.AutoField(primary_key=True)
    intituleProd = models.CharField(max_length=200)
    prixUnitaireProd = models.DecimalField(max_digits=10, decimal_places=2)
    dateProd = models.DateField(auto_now=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="produits", null=True, blank=True)
    statutProd = models.ForeignKey(Statut, on_delete=models.CASCADE, related_name="produitStatut", null=True, blank=True)
    
    def clean(self):
        if self.prixUnitaireProd < 0:
            raise ValidationError({'prixUnitaireProd': "Le prix ne peut pas être négatif."})
        if not self.intituleProd.strip():
            raise ValidationError({'intituleProd': "Le nom du produit ne peut pas être vide."})
        if Produit.objects.filter(intituleProd=self.intituleProd).exclude(pk=self.pk).exists():
            raise ValidationError({'intituleProd': "Un produit avec ce nom existe déjà."})

    def __str__(self):
        return self.intituleProd

class Rayon(models.Model):

    idRayon = models.AutoField(primary_key=True)
    nomRayon = models.CharField(max_length=100)

    def __str__(self):
        return self.nomRayon

class Contenir(models.Model):
    refProd = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="contenirP")
    idRayon = models.ForeignKey(Rayon, on_delete=models.CASCADE, related_name="contenirR")
    qte = models.IntegerField()

    class Meta:
        unique_together = (('refProd', 'idRayon'),)

    def clean(self):
        # Validation pour la quantité
        if self.qte < 0:
            raise ValidationError({'qte': "La quantité ne peut pas être négative."})

    def __str__(self):
        return f"{self.refProd.intituleProd} dans {self.idRayon.nomRayon} : {self.qte}"



