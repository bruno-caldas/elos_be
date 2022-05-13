from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'eventos'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.carrega_eventos, name='eventos'),
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)