from django.shortcuts import render
from django.views.generic import View



class Que_es(View):
	def get(self,request):
		template_name="blog-single.html"	
		
		return render(request,template_name)
