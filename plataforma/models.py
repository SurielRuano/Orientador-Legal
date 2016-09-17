from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# Create your models here.
class Colaborador(models.Model):


	nombre = models.CharField(max_length=100)
	email = models.EmailField(max_length=254)
	telefono = models.PositiveIntegerField()
	carrera = models.CharField(max_length=100)
	descripcion_profesional = models.CharField(max_length=200)

	def __str__(self):

		return self.nombre




class Categoria(models.Model):


	nombre_cat = models.CharField(max_length=100)
	descripcion_cat = models.TextField(max_length=400)
	slug = models.SlugField(max_length=200)
	imagen_cat = models.CharField(max_length=100,blank=True,null=True)

	
	def get_absolute_url(self):
		return reverse('categoria:listaArticulos', args=[self.slug])

	def __str__(self):

		return self.nombre_cat




class Articulo(models.Model):


	titulo = models.CharField(max_length=100)
	
	descripcion_breve = models.TextField(max_length=250,null=False)
	cuerpo_principal = models.TextField(max_length=2000,null=False)
	que_hacer = models.TextField(max_length=2000,null=True,blank=True)
	que_evitar = models.TextField(max_length=2000,null=True,blank=True)
	fecha = models.DateTimeField(auto_now=True)
	categoria = models.ManyToManyField(Categoria,related_name='articulos')
	colaborador = models.ForeignKey(Colaborador, related_name='articulos')
	aprobar = models.BooleanField(default=False)

	def __str__(self):

		return self.titulo