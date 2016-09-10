from django.db import models
from django.conf import settings

# Create your models here.


class Perfil(models.Model):

	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	tel = models.CharField(max_length=10,blank=True,null=True)
	fecha_nacimiento = models.DateField(blank=True,null=True)
	photo = models.ImageField(upload_to= "colaboradores/%Y/%m", blank=True, null=True)


	def __str__(self):

		return 'Perfil de usuario {}'.format(self.user.username)


class SolicitudColaboracion(models.Model):


	CHOICES=(('si','Si'),('no','No'))

	name = models.CharField(max_length=150)
	licenciatura_leyes = models.CharField(max_length=2,choices=CHOICES)
	telefono = models.CharField(max_length=10,blank=True,null=True)
	fecha_nacimiento = models.DateField(blank=True,null=True)
	fecha_solicitud = models.DateTimeField(auto_now=True)


	def __str__(self):

		return 'Solicitud - {}'.self.name

