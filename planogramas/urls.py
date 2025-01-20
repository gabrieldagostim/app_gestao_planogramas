from django.urls import path
from . import views

urlpatterns = [
    path('criar_planograma', views.criar_planograma, name='criar_planograma'),
    path('listar_planogramas', views.listar_planograma, name='listar_planogramas'),
    path('planogramas/editar/<int:id>/', views.editar_planograma, name='editar_planograma'),
    path('planogramas/excluir/<int:id>/', views.excluir_planograma, name='excluir_planograma'),
]
