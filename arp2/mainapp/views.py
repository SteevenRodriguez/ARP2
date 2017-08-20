from django.shortcuts import render, redirect, reverse

from .forms import *
from .models import *


# Create your views here.
def NuevoRepuesto(request):
	if request.method == "POST":
		form = RepuestoForm(request.POST)
		print(form.errors)
		if form.is_valid():
			form.save()
			return redirect('dato-repuesto')
	elif request.method == "GET":
		form = RepuestoForm()
	return render(request, 'baseform.html', {'objeto': 'Repuesto', 'form': form})

	# Create your views here.
def NuevoDato(request):
	if request.method == "POST":
		form = DatosForm(request.POST)
		print(form.errors)
		if form.is_valid():
			form.save()
			return render(request, 'baseform.html', {'objeto': 'Datos', 'form': form})
	elif request.method == "GET":
		form = DatosForm()
	return render(request, 'baseform.html', {'objeto': 'Datos', 'form': form})


def verRepuestos(request):
	repuesto = Repuesto.objects.all()
	nrepuestos= len(repuesto)
	return render(request, 'listRepuesto.html', {'nrepuestos':nrepuestos, 'repuesto':repuesto})


def home(request):
	return render(request,'home.html')