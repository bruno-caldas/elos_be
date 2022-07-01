from django.urls import path
from django.conf.urls import url
from doadores import views
from .views import DoadoresList, DoadoresUpdate, DoacaoList
from django.contrib.auth import views as auth_views

# app_name = "doadores"


urlpatterns = [
    url(r'^doador/$', views.doadoresApi),
    url(r'^doador/([0-9]+)$', views.doadoresApi),
    path('listar/', DoadoresList.as_view(), name='listar'),
    path('ldoacao/', DoacaoList.as_view(), name='ldoacao'),
    path('editar/doadores/<int:pk>/', DoadoresUpdate.as_view(), name='editar-doadores'),
]
