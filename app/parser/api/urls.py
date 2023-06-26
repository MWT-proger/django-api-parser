from django.urls import path, include

urlpatterns = [
    path("v1/", include("parser.api.v1.urls")),
]
