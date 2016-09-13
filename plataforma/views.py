from django.shortcuts import render
from django.views.generic import View
from .models import Categoria



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
