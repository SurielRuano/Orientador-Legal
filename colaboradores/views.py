from django.shortcuts import render,redirect

from django.views.generic import View

from .models import Perfil
from .forms import SolicitudColaboracionForm

# Create your views here.



class Solicitud_colaboracion(View):
	def get(self,request):

		template_name = 'registro/registro.html'
		form = SolicitudColaboracionForm()

		context = {'form':form}

		return render (request,template_name,context)
