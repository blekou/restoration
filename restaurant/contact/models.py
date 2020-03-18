from django.db import models

# Create your models here.
class Contact(models.Model):

    nom = models.CharField(max_length=225)
    prenom =models.CharField(max_length=225)
    sujet=models.CharField(max_length=225)
    message=models.TextField()
    email=models.EmailField()

    class Meta():
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.nom




class Newsletter(models.Model):

    email=models.EmailField()

    class Meta():
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletter'

    def __str__(self):
        return self.email
