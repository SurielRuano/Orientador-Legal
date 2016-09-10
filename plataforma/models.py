from django.db import models

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


	categoria = models.CharField(max_length=100)
	

	def __str__(self):

		return self.categoria




class Articulo(models.Model):


	articulo = models.CharField(max_length=100)
	contenido = models.CharField(max_length=100)
	categoria = models.ManyToManyField(Categoria)
	colaborador = models.ForeignKey(Colaborador)

	def __str__(self):

		return self.articulo