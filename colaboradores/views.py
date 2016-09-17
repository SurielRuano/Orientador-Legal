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

	def post(self,request):
		template_name = "registro/registro.html"
		template_name_success = 'registro/solicitud_exitosa.html'

		new_solicit_form = SolicitudColaboracionForm(request.POST)

		if new_solicit_form.is_valid():

			new_solicit = new_solicit_form.save(commit=False)
			new_solicit.save()
			return render(request,template_name_success)

		else:
			context = {

			'form': new_solicit_form
			}
			return render(request,template_name,context);