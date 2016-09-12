from django.shortcuts import render
from django.views.generic import View



class Que_es(View):
	def get(self,request):
		template_name="que-es.html"	
		
		return render(request,template_name)


class Categorias(View):
	def get(self,request):
		template_name = 'categorias.html'

		return render(request,template_name)
