from django.shortcuts import render
from django.views.generic import View
from .models import Categoria, Articulo




class Que_es(View):
	def get(self,request):
		template_name="que-es.html"	
		
		return render(request,template_name)


class Categorias(View):
	def get(self,request):
		template_name = 'categorias.html'

		cat = Categoria.objects.all()

		context = {'cat':cat}

		return render(request,template_name,context)


class ListaCategoria(View):
	def get(self,request,slug):
		template_name = "categoria-articulos.html"
		cat =  Categoria.objects.filter(slug = slug)
		# articulos = Articulo.objects.select_related()
		slug = slug
		articulos = Articulo.objects.filter(categoria = cat) 		

		context = {'categoria':cat, 'articulos':articulos,"slug":slug}
		return render(request,template_name,context)


	def post(self,request,slug):
			
		template_name = "categoria-articulos.html"
		cat =  Categoria.objects.filter(slug = slug)
		# articulos = Articulo.objects.select_related()
		articulos = Articulo.objects.filter(categoria = cat) 		

		context = {'categoria':cat, 'articulos':articulos}
		return render(request,template_name,context)

class Detalle_articulo(View):
	def get(self,request,slug,slug2):

		template_name = "detalle_articulo.html"
		art =  Articulo.objects.filter(slug = slug2)
		# articulos = Articulo.objects.select_related()
		

		context = {'articulo':art}
		return render(request,template_name,context)