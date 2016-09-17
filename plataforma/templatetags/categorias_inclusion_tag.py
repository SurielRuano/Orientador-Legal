from django import template
register = template.Library()
from plataforma.models import Categoria, Articulo




## tag que recibe una variable y renderiza un pequeno template html
@register.inclusion_tag('template_tags/categorias_sidebar.html')
def show_categorias(count=6):
	categorias= Categoria.objects.all().order_by('-nombre_cat')[:count]
	return {
	'categorias':categorias
	}

## tag que recibe una variable y renderiza un pequeno template html
@register.inclusion_tag('template_tags/categorias_footer.html')
def show_categorias_footer(count=6):
	categorias= Categoria.objects.all().order_by('-nombre_cat')[:count]
	return {
	'categorias':categorias
	}


## tag que recibe una variable y renderiza un pequeno template html
@register.inclusion_tag('template_tags/articulos_recientes.html')
def show_articulos_footer(count=6):
	articulos= Articulo.objects.all().order_by('-fecha')[:count]
	return {
	'articulos':articulos
	}


## tag que recibe una variable y renderiza un pequeno template html
@register.inclusion_tag('template_tags/articulos_sidebar.html')
def show_articulos_sidebar(count=6):
	articulos= Articulo.objects.all().order_by('-fecha')[:count]
	return {
	'articulos':articulos
	}

