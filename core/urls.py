
from django.contrib import admin
from django.urls import path, include

from core.views import retornar_frase

urlpatterns = [
    path('', retornar_frase ),

]
