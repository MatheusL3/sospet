from django.contrib import admin
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import path, include
from django.views.generic import RedirectView
from sospet import settings
from sospet.core import views

# from core import settings


urlpatterns = [

    path('login/', views.login_user),
    path('pet/all/', views.list_all_pets, name='home'),
    path('pet/register/', views.register_pet, name='cadastrar'),
    path('pet/register/submit/', views.set_pet),
    # path('pet/detail/<id>/', views.pet_detail),
    # path('pet/delete/<id>/', views.pet_delete),
    path('pet/<action>/<id>/', views.pet_generic),

    path('pet/user/', views.list_user_pets, name='meus-pets'),
    path('login/submit/', views.submit_login),
    path('logout/', views.logout_user),
    path('', RedirectView.as_view(url='pet/all/'))
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
