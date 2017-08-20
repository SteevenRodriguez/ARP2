from .models import *
from django import forms
from django.forms import Textarea

class RepuestoForm(forms.ModelForm):
	class Meta:
		model = Repuesto
		fields = ['nombre','foto','descripcion1','descripcion2','descripcion3','cantidad']
		label = {'nombre':'Ingrese nombre del repuesto',
		'foto':'Ingrese foto del repuesto',
		'descripcion 1':'Llene la descripcion #1',
		'descripcion 2':'Llene la descripcion #2',
		'descripcion 3':'Llene la descripcion #3',
		'cantidad':'Ingrese una cantidad'
		}
		widgets = {
            'descripcion1': Textarea(attrs={'class':'form-textarea-control','cols': 80, 'rows': 2}),
            #'descripcion1': label(attrs={'class':'form-label-control','cols': 80, 'rows': 2}),
            'descripcion2': Textarea(attrs={'class':'form-textarea-control','cols': 80, 'rows': 2}),
            'descripcion3': Textarea(attrs={'class':'form-textarea-control','cols': 80, 'rows': 2}),
		}
