from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'blog'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.carrega_posts, name='posts'),
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)