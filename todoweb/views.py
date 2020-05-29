from django.shortcuts import render
from django.utils import timezone
from .models import List, Activity
from django.shortcuts import render, get_object_or_404
#from .forms import PostForm, CommentForm, RegisterForm
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