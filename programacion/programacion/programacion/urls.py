from django.urls import path, include
from django.conf.urls import url
from .views import *



urlpatterns = [    
    url(r'^programacion',programacion_api_view),
]