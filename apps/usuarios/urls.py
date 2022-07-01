from django import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'usuarios'
urlpatterns = [
    path('cadastro',views.cadastro,name='cadastro'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logout,name='logout')
]
