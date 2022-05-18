from django.apps import apps
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import permissions

from parceiros.models import Parceiros
#./apps.arceiros.models import Parceiros
from ..serializers import *

# Easy way of controling the API
# @api_view(['GET'])
# def getData(request):
#     dados = Parceiros.objects.all()
#     serializer = ParceirosSerializer(dados, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def addData(request):
#     serializer = ParceirosSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# Documentation says to use the following to control de API
class controleParceiros(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Parceiros.objects.all()
    serializer_class = ParceirosSerializer
    # permission_classes = [permissions.IsAuthenticated]

