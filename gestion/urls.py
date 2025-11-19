from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('tarea/<int:tarea_id>/', views.detalle_tarea, name='detalle_tarea'),
    
    # Rutas para el CRUD
    path('tarea/nueva/', views.crear_tarea, name='crear_tarea'),
    path('tarea/<int:tarea_id>/editar/', views.editar_tarea, name='editar_tarea'),
    path('tarea/<int:tarea_id>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
]