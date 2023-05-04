from django.contrib import admin
from .models import Client, Rapport, Presence

# # Register your models here.

admin.site.register([   
    Client,
    Rapport,
    Presence 
]
)
