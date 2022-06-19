from django.conf.urls import url
from doadores import views

urlpatterns = [

    url(r'^doador/$', views.doadoresApi),
    url(r'^doador/([0-9]+)$', views.doadoresApi)
    
]