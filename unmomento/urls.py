"""unmomento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from home import urls as homeUrls
from plataforma import urls as platUrls
from colaboradores import urls as colabUrls
from django.conf import settings
from django.views.static import serve
from plataforma import views
urlpatterns = [
	url(r'^',include(homeUrls)),
    url(r'^admin/', admin.site.urls),
    url(
    regex=r'^media/(?P<path>.*)$',
    view=serve,
    kwargs={'document_root':settings.MEDIA_ROOT}),

    url(r'^que_es/',include(platUrls)),
    url(r'^colaboradores/',include(colabUrls,namespace='colaboradores')),
    url(r'^articulo/',include(platUrls,namespace='articulo')),
    url(r'^categorias/',views.Categorias.as_view(),name='categorias'),
    url(r'^categoria/',include(platUrls,namespace='categoria')),
]
