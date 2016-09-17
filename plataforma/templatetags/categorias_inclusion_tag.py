from django import template
register = template.Library()
from plataforma.models import Categoria




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

