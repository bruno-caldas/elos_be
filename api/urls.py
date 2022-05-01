from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.controleParceiros)

urlpatterns = [
    # path('', views.getData),
    # path('add/', views.addData)
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]