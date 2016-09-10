from django.contrib import admin
from .models import Colaborador, Articulo, Categoria
# Register your models here.


class ArticulosFiltro(admin.ModelAdmin):

	

	list_display=['articulo','colaborador']
	list_filter=['articulo','categoria']

admin.site.register(Colaborador)
admin.site.register(Articulo, ArticulosFiltro)
admin.site.register(Categoria)