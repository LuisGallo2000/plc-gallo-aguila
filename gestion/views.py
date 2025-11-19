from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarea
from .forms import TareaForm

# READ (Lista)
def lista_tareas(request):
    tareas = Tarea.objects.all().order_by('-fecha_creacion')
    contexto = {'tareas': tareas}
    return render(request, 'gestion/lista_tareas.html', contexto)

# READ (Detalle)
def detalle_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    contexto = {'tarea': tarea}
    return render(request, 'gestion/detalle_tarea.html', contexto)

# CREATE
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    
    contexto = {'form': form}
    return render(request, 'gestion/tarea_form.html', contexto)

# UPDATE
def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('detalle_tarea', tarea_id=tarea.id)
    else:
        form = TareaForm(instance=tarea)
    
    contexto = {'form': form}
    return render(request, 'gestion/tarea_form.html', contexto)

# DELETE
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('lista_tareas')
    
    contexto = {'tarea': tarea}
    return render(request, 'gestion/tarea_confirm_delete.html', contexto)