from django.shortcuts import render
import requests, json
from rest_framework import viewsets
from .models import Despesa
from .serializers import DespesaSerializer

def home(request):
    response = requests.get('http://www.transparencia.gov.br/api-de-dados/despesas/documentos?gestao=15222&dataEmissao=12%2F12%2F2017&fase=3&pagina=1')
    data = json.loads(response.content)
    print(data[0]['valor'])
    return render(request, 'despesas.html', {
        'valor': data[0]['valor'],
    })




class DespesaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer