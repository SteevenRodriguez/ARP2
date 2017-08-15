from .models import *
from django import forms

class RepuestoForm(forms.ModelForm):
	class Meta:
		model = Repuesto
		fields = ['nombre','foto','descripcion','cantidad']
		label = {'nombre':'Ingrese nombre del repuesto',
		'foto':'Ingrese foto del repuesto',
		'descripcion':'Llene la descripcion',
		'cantidad':'Ingrese una cantidad'
		}

class DatosForm(forms.ModelForm):
	class Meta:
		model= Datos
		fields = ['repuesto','descripcion1','descripcion2','descripcion3']
		label ={
			'repuesto':'Asigne un repuesto',
			'descripcion1':'Descripcion',
			'descripcion2':'Descripcion',
			'descripcion3':'Descripcion'
			}		
		
