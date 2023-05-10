from django.db import models
from authentification.models import Utilisateur




# Create your models here.





class Client(models.Model):


    choices = (
    ('auto', 'Auto'),
    ('voyage', 'voyage'),
    ('Maladie', 'Maladie'),
    ('Tout risque', 'Tout risque'),
    ('Caution', 'Caution'),
    )
    nom = models.CharField(max_length=200, null=False)
    prenom = models.CharField(max_length=200, null=False)
    adresse = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=False, )
    date_naiss = models.DateField()
    tel = models.CharField(default=0, max_length=200)
    typeAssur = models.CharField(null= False, max_length=200, choices=choices )
    autre = models.TextField(null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-created_at',)

    def __str__(self):
        return f'{self.nom} {self.id}'   

class Presence(models.Model):
    jour_fiche = models.DateTimeField()
    heure_arri = models.DateTimeField()              
    heure_dep = models.DateTimeField()              
    deb_pause = models.DateTimeField()              
    fin_pause = models.DateTimeField()
    utilisateur = models.ForeignKey(Utilisateur, on_delete = models.CASCADE, default=0) 
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


    class Meta:
        ordering=('-created_at',)

    def __str__(self):
        return f'{self.jour_fiche} {self.id}'   

class Rapport(models.Model):
    date = models.DateTimeField()
    libelle = models.TextField(max_length=200, null=False)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-created_at',)

    def __str__(self):
        return f'{self.date} {self.id}' 

