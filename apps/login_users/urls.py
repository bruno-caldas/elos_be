from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, carrega_cep, pesquisa_cep
from . import views

# app_name = 'login_users'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name = 'login_users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'login_userf/logout.html'), name='logout'),
    path('signup/',UsuarioCreate.as_view(template_name = 'login_users/signup.html'), name='signup'),
    path('via_cep', carrega_cep, name='cep'),
    path('pesquisa_cep',pesquisa_cep,name="via_cep"),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

