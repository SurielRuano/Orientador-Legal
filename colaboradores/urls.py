from django.conf.urls import url, include
from django.conf import settings
from . import views



urlpatterns = [
	url(r'^solicitud-colaboracion/$', views.Solicitud_colaboracion.as_view(),name="solicit"),
	
]