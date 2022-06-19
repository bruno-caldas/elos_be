from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rede_social.views import carrega_cep, pesquisa_cep
from . import views

app_name = 'rede_social'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', carrega_cep, name='cep'),
    path('pesquisa_cep', pesquisa_cep,name="via_cep"),
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)