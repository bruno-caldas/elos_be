from rest_framework.response import Response
from rest_framework.decorators import api_view
from parceiros.models import Parceiros
from .serializers import ParceirosSerializer

@api_view(['GET'])
def getData(request):
    dados = Parceiros.objects.all()
    serializer = ParceirosSerializer(dados, many=True)
    return Response(serializer.data)