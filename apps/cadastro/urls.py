from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'cadastro'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.mural_animais, name='mural_animais'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('form/', views.test_form, name='test_form'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

