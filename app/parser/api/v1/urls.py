from django.urls import path
from parser import views

urlpatterns = [
    path('tnved', views.tnved_view),
    path('tnved_okpd', views.tnved_okpd),
    path('trts', views.trts),
]
