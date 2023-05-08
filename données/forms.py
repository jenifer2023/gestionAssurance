from django.forms import ModelForm, Textarea
from . import models
from .models import Rapport
from django import forms


class RapportForm(ModelForm):
    class Meta:
        model = Rapport
        fields = ('date', 'libelle',)  
        widgets = {

            'lebelle': Textarea(attrs={'cols':50,'rows':10}),
            # 'date': SelectDateWidget(),
        }

        
          