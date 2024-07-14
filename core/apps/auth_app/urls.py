from django.urls import path, include
from djoser import views as djoser_views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
