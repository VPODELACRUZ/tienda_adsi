from django.urls import path
from .views import *


urlpatterns = [
	path('logout/',vista_logout),
	path('register/',vista_register, name="vista_register"),
	path('login/',vista_login, name="vista_login"),
	path('tanks_for_register/',vista_tanks_for_register),
	path('',vista_inicio),
	path('about/',vista_about),
	path('bts/',vista_bts),
	path('casa/',vista_casa),
	path('contacto/',vista_contacto),
	path('lista_producto/',vista_lista_producto, name='vista_lista_producto'), 
	path('agregar_producto/',vista_agregar_producto, name='vista_agregar_producto'),
	path('crear_perfil/',vista_crear_perfil, name='vista_crear_perfil'), 
	path('ws/productos/',ws_productos_vista,name='ws_productos_vista'),

]