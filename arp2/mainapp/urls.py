from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^NuevoRepuesto/$', NuevoRepuesto, name="nuevo-repuesto"),
    url(r'^verRepuestos/$', verRepuestos, name="verRepuestos"),
    url(r'^editarRepuesto/(?P<item>\d+)$', Repuesto_editar, name='repuesto_editar'),
    url(r'^eliminarRepuesto/(?P<item>\d+)$', Repuesto_eliminar, name='repuesto_eliminar'),
]
