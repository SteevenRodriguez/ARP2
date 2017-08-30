from django.shortcuts import render, redirect, reverse, get_object_or_404

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

def Repuesto_editar(request, item):
    repuesto = get_object_or_404(Repuesto, pk=item)
    if request.method == "GET":
    	form = RepuestoForm(instance=repuesto)
    else:
	    form = RepuestoForm(request.POST, request.FILES, instance=repuesto)
	    if form.is_valid():
	        form.save()
	        return redirect('verRepuestos')
    return render(request, 'baseform.html', {'form':form, 'tipo_objeto':"repuesto"})
   

def Repuesto_eliminar(request, item):
    repuesto = get_object_or_404(Repuesto, pk=item)
    repuestos = Repuesto.objects.all()
    if request.method=='GET':
    	print(repuesto)
        repuesto.delete()
        return redirect('verRepuestos')
    return render(request,'listRepuesto.html',{'object_list': repuestos,'object':repuesto, 'eliminar': 'True','tipo_objeto':"repuesto"})