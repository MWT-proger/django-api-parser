from django.urls import path
from parser import views

urlpatterns = [
    path('tnved', views.tnved_view),
]
