from .models import Repuesto
from django import forms

class RepuestoForm(forms.ModelForm):
	class Meta:
		model = Repuesto
		fields = ['nombre','foto','descripcion1','descripcion2','descripcion3','cantidad']
		labels = {
			'nombre':'Ingrese nombre del repuesto',
			'foto':'Ingrese foto del repuesto',
			'descripcion1':'Llene la descripcion #1',
			'descripcion2':'Llene la descripcion #2',
			'descripcion3':'Llene la descripcion #3',
			'cantidad':'Ingrese una cantidad'
		}
		widgets = {
			'foto': forms.FileInput(),
            'descripcion1': forms.Textarea(attrs={'class':'form-textarea-control','cols': 80, 'rows': 2}),
            'descripcion2': forms.Textarea(attrs={'class':'form-textarea-control','cols': 80, 'rows': 2}),
            'descripcion3': forms.Textarea(attrs={'class':'form-textarea-control','cols': 80, 'rows': 2}),
		}
