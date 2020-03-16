from django.urls import path
from . import views
from Native_idoms.views import data, district,chondokotha

urlpatterns = [
    path('', views.home),
    path('data/', data),
    path('district/', district),
    path('chondokotha/', chondokotha),
]
