from django import forms
from django.contrib.auth.models import User
from .models import Perfil,SolicitudColaboracion

class SolicitudColaboracionForm(forms.ModelForm):

	class Meta:
		model = SolicitudColaboracion
		fields = ('name','licenciatura_leyes','telefono','fecha_nacimiento')

