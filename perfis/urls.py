from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('perfis/<int:perfil_id>', views.exibir, name='exibir'),
	path('perfis/<int:perfil_id>/convidar', views.convidar, name='convidar')
	# re_path(r'^perfis/\d+$', views.exibir, name='perfis')
]