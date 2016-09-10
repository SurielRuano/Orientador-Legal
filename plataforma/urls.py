from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$',views.Que_es.as_view(),name='que_es'),

]