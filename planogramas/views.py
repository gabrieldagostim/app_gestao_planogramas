from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Planograma
from .forms import PlanogramaForm 

def listar_planograma(request):
    planogramas = Planograma.objects.all()
    return render(request, 'listar_planogramas.html', {'planogramas': planogramas})

def criar_planograma(request):
    if request.method == 'POST':
        form = PlanogramaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_planogramas')
    else:
        form = PlanogramaForm()
    return render(request, 'criar_planograma.html',{'form': form})

def editar_planograma(request, id):
    planograma = get_object_or_404(Planograma, id=id) # TODO criar função
    if request.method == 'POST':
        # lógica para salvar as alterações
        pass
    return render(request, 'editar_planograma.html', {'planograma': planograma})



def excluir_planograma(request, id):
    planograma = get_object_or_404(Planograma, id=id)
    planograma.delete()
    return redirect('listar_planogramas')  # Redirecione para a lista de planogramas
