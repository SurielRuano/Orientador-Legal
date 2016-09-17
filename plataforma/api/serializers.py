from rest_framework import serializers
from ..models import Articulo


class ArticuloSerializer(serializers.ModelSerializer):
		class Meta:
			model = Articulo
			field = ('id','titulo','descripcion_breve','cuerpo_principal','que_hacer','que_evitar','fecha','categoria','colaborador','aprobar','slug')