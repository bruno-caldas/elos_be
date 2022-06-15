from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate
from . import views

# app_name = 'login_users'

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(
        template_name = 'login_users/form.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('signup/', UsuarioCreate.as_view(template_name = 'login_users/formSIGNUP.html'
    ), name='signup'),

    # path('', carrega_cep, name='cep'),
    # path('pesquisa_cep/', Pesquisa,name="via_cep"),

   # path('', views.carrega_login, name='carrega_login'),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

