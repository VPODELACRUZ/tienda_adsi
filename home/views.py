from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
def vista_about(request):
	return render(request,'about.html')

def vista_bts(request):
	return render(request,'bts.html')

def vista_casa(request):
	return render(request,'casa.html')

def vista_lista_producto (request):
	productos = Producto.objects.all()
	return render(request, 'lista_producto.html', locals())


def vista_agregar_producto (request):
	if request.method == 'POST':
		formulario = agregar_producto_form(request.POST,request.FILES)
		if formulario.is_valid:
			prod = formulario.save(commit= False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/lista_producto/')
	else:
			formulario = agregar_producto_form()
	return render(request, 'agregar_producto.html', locals())





def vista_contacto(request):
	info_enviado = False
	email = ""
	title = ""
	text = ""
	if request.method =="POST":
		formulario=contacto_form(request.POST)
		if formulario.is_valid():
			info_enviado=True
			email=formulario.cleaned_data['correo']
			title=formulario.cleaned_data['titulo']
			text=formulario.cleaned_data['texto']
	else:#cualuqier metodo va aqui
		formulario = contacto_form()
	return render(request,'contacto.html',locals())

def vista_login (request):
	usu =''
	cla =''
	if request.method == 'POST':
		formulario= login_form (request.POST)
		if formulario.is_valid():
			usu=formulario.cleaned_data['usuario']
			cla=formulario.cleaned_data['clave']
			usuario= authenticate(username=usu,password=cla)
			if usuario is not None and usuario.is_active:
				login(request,usuario)
				return redirect('/')
			else:
				msj="usuario o claves no coinciden"
	formulario=login_form
	return render(request,'login.html',locals())

def vista_logout(request):
	logout(request)
	return redirect('/login/')


def vista_register (request):
	formulario=register_form()
	if request.method == 'POST':
		formulario=register_form(request.POST)
		if formulario.is_valid():
			usuario=formulario.cleaned_data['username']
			correo=formulario.cleaned_data['email']
			password_1=formulario.cleaned_data['password_1']
			password_2=formulario.cleaned_data['password_2']
			u=User.objects.create_user(username=usuario,email=correo,password=password_1)
			u.save()
			return render(request,'tanks_for_register.html',locals())
		else:
			return render(request,'register.html',locals())
	return render(request,'register.html',locals())



def vista_tanks_for_register(request):
	return render(request,'tanks_for_register.html')

def vista_inicio(request):
	return render(request,'inicio.html')

def vista_crear_perfil(request):
	form_1= register_form()
	form_2= perfil_form()
	if request.method=='POST':
		form_1= register_form(request.POST)
		form_2= perfil_form(request.POST, request.FILES)
		if form_1.is_valid() and form_2.is_valid():
			usuario=form_1.cleaned_data['username']
			correo=form_1.cleaned_data['email']
			password_1=form_1.cleaned_data['password_1']
			password_2=form_1.cleaned_data['password_2']
			u=User.objects.create_user(username=usuario,email=correo,password=password_1)
			u.save()

			y=form_2.save(commit=False)
			y.user=u
			y.save()
			msg="gracias perro por registrarse"


	return render(request,'crear_perfil.html',locals())

def ws_productos_vista(request):
	data=serializers.serialize('xml',Producto.objects.filter(status = True))
	return HttpResponse(data, content_type='application/xml')

	

