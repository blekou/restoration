from django.db import models

# Create your models here.

class CompteSocial(models.Model):

    nom = models.CharField(max_length=225)
    ICONE = [
    ("facebook", "fa-facebook"),
    ("googleplus", "fa-googleplus"),
    ("instagram", "fa-instagram"),
    ("linkedin", "fa-linkedin"),
    ]

    liens = models.URLField()
    icones =models.CharField(choices = ICONE,max_length=30)

    date_add = models.DateTimeField(auto_now = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta():
        verbose_name = "Compte social"
        verbose_name_plural = "Compte socials"

    def __str__(self):
        return self.nom


class Site_info(models.Model):

    lien= models.URLField()
    map_url = models.TextField(max_length=225)
    email = models.EmailField()
    logo = models.CharField(max_length=225)

    date_add = models.DateTimeField(auto_now = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta():
        verbose_name = "infos du site"
        verbose_name_plural = "infos du sites"

    def __str__(self):
        return self.lien


class Presentation(models.Model):
    nom = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField()
    video = models.TextField()

    date_add = models.DateTimeField(auto_now = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta():
        verbose_name = "Presentation"
        verbose_name_plural= "Presentations"

    def __str__(self):
        return self.nom

class Temoignage(models.Model):

    photo = models.TextField()
    nom = models.CharField(max_length=225)
    prenom = models.CharField(max_length=225)
    message =models.TextField()

    date_add = models.DateTimeField(auto_now = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta():
        verbose_name = "Temoignage"
        verbose_name_plural= "Temoignages"

    def __str__(self):
        return self.nom
