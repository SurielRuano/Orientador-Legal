from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$',views.Que_es.as_view(),name='que_es'),
	url(r'^(?P<slug>[-\w]+)/$',views.ListaCategoria.as_view(),name='listaArticulos'),
	url(r'^(?P<slug>[-\w]+)/(?P<slug2>[-\w]+)/$',views.Detalle_articulo.as_view(),name='detalleArticulo'),

]