from django.conf.urls import url
from doadores import views

urlpatterns = [

    url(r'^doador/$', views.doadoresApi),
    url(r'^doador/([0-9]+)$', views.doadoresApi)
<<<<<<< HEAD

=======
    
>>>>>>> 18f5c8a (Criação login de usuarios, api cadastro de doadores e doação)
]