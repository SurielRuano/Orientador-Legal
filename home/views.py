from django.shortcuts import render
from django.views.generic import View
from plataforma.models import Categoria



class Home(View):
	def get(self,request):
		template_name="home/home.html"
		cat=Categoria.objects.all()

		context = {'categoria':cat}
		
		return render(request,template_name,context)
