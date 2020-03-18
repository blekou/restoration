from django.db import models

# Create your models here.


#models articles
class Produit(models.Model):

    nom = models.CharField(max_length=225)
    description = models.TextField(max_length=225)
    image = models.ImageField()
    prix = models.FloatField()
    specialite = models.CharField(max_length=225)

    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)


    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produit"

    def __str__(self):
        return self.nom


#models categories
class Categorie(models.Model):

    nom = models.CharField(max_length=225)
    description = models.TextField(max_length=225)
    image = models.ImageField()


    date_add = models.DateTimeField(auto_now = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)


    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.nom + self.image
