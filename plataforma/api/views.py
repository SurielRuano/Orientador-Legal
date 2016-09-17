from rest_framework import generics
from ..models import Articulo
from .serializers import ArticuloSerializer


class ArticuloListView(generics.ListAPIView):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloSerializer

class ArticuloDetailView(generics.RetrieveAPIView):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloSerializer