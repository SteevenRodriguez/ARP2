from django.shortcuts import render, redirect, reverse

from .forms import *
from .models import *


# Create your views here.
def NuevoRepuesto(request):
	if request.method == "POST":
		print(request.FILES)
		form = RepuestoForm(request.POST, request.FILES)
		print(form.errors)
		if form.is_valid():
			form.save()
			return redirect('home')
	elif request.method == "GET":
		form = RepuestoForm()
	return render(request, 'baseform.html', {'objeto': 'Repuesto', 'form': form})


def verRepuestos(request):
	repuesto = Repuesto.objects.all()
	nrepuestos= len(repuesto)
	return render(request, 'listRepuesto.html', {'nrepuestos':nrepuestos, 'repuesto':repuesto})


def home(request):
	return render(request,'home.html')