from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'login_users'
urlpatterns = [
    path('', views.carrega_login, name='carrega_login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

