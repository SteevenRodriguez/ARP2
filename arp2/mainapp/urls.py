from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^NuevoRepuesto/$', NuevoRepuesto, name="nuevo-repuesto"),
    url(r'^verRepuestos/$', verRepuestos, name="verRepuestos"),
]