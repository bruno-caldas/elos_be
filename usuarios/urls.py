from django.conf import settings
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views

app_name = 'usuarios'

urlpatterns = [

    path('', auth_views.LoginView.as_view(
        template_name = 'usuarios/index.html'
    ), name='login'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



