from django.conf.urls import url
from  . import  views


urlpatterns = [
	
	url(r'^articulo/$',
		views.ArticuloListView.as_view(),
		name='api_articulo_lista'),

	url(r'^articulo/(?P<pk>\d+/)$',
		views.ArticuloDetailView.as_view(),
		name = 'api_articulo_detalle'),
	
]