from django.urls import path, include
from sospet.places import views


urlpatterns = [
    path('places/', views.places, name='Lugares'),
]
