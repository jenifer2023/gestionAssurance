from django.forms import ModelForm, Textarea, DateTimeInput
from . import models
from .models import Rapport, Client
from django import forms


class RapportForm(ModelForm):
    class Meta:
        model = Rapport
        fields = ('date', 'libelle',)  
        widgets = {

            'lebelle': Textarea(attrs={'cols':50,'rows':10}),
            'date': DateTimeInput(),
        }


class ClientForm(forms.Form):

    # class Meta:
    #     model = Client
    #     fields = ('nom','adresse','email', 'date_naiss', 'tel', "typeAssur", 'autre')

    choices = (
    ('auto', 'Auto'),
    ('voyage', 'voyage'),
    ('Maladie', 'Maladie'),
    ('Tout risque', 'Tout risque'),
    ('Caution', 'Caution'),
    )

    nom = forms.CharField(max_length=200,label='Nom/Raison Social' )
    # prenom = forms.CharField(max_length=200,label='Nom/Raison Social')
    adresse = forms.CharField(max_length=200, label='adresse')
    email = forms.EmailField(max_length=200,label='Email')
    date_naiss = forms.DateField(label='Date de Naissance')
    tel = forms.CharField( max_length=200, label='Téléphone')
    typeAssur = forms.ChoiceField(choices=choices, label='Type Assurance' )
    autre = forms.CharField(widget=forms.Textarea(attrs={'cols':30,'rows':5})) 
          