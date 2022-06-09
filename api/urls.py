from django.urls import include, path
from rest_framework import routers

#from api.views.carrega_parceiros import ParceirosViewSet
from .views import *

router = routers.DefaultRouter()
#router.register(r'',views.controleParceiros)
router.register('parceiros', ParceirosViewSet, basename='Parceiros')
router.register('eventos', EventosViewSet, basename='Eventos')
router.register('blog', PostViewSet, basename='Blog')

urlpatterns = [
    # path('', views.getData),
    # path('add/', views.addData)
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]