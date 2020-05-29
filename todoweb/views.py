from django.shortcuts import render
from django.utils import timezone
from .models import List, Activity
from django.shortcuts import render, get_object_or_404
from .forms import ListForm, ActivityForm, RegisterForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def lists(request):
    lists = List.objects.filter(idUser=request.user).order_by('-id')
    return render(request, 'todoweb/lists.html', {'lists' : lists})

@login_required
def list_detail(request, pk):
    list = get_object_or_404(List, pk=pk)
    return render(request, 'todoweb/list_detail.html', {'list': list})


@login_required
def list_new(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            list.idUser = request.user
            list.save()
            return redirect('list_detail', pk=list.pk)
    else:
        form = ListForm()
        return render(request, 'todoweb/list_edit.html', {'form': form})


@login_required
def list_new(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            list.idUser = request.user
            list.save()
            return redirect('list_detail', pk=list.pk)
    else:
        form = ListForm()
        return render(request, 'todoweb/list_edit.html', {'form': form})



@login_required
def list_edit(request, pk):
    list = get_object_or_404(List, pk=pk)

    if request.method == "POST":
        form = ListForm(request.POST, instance=list)
        if form.is_valid():
            list = form.save(commit=False)
            list.idUser = request.user
            list.save()
            return redirect('list_detail', pk=list.pk)
    else:
        form = ListForm(instance=list)
        return render(request, 'todoweb/list_edit.html', {'form': form, 'edit' : 'edit'})


@login_required
def list_remove(request, pk):
    list = get_object_or_404(List, pk=pk)
    list.delete()
    return redirect('lists')