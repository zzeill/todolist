from django.shortcuts import render
from django.utils import timezone
from .models import List, Activity
from django.shortcuts import render, get_object_or_404
#from .forms import PostForm, CommentForm, RegisterForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def lists(request):
    lists = List.objects.order_by('-id')
    return render(request, 'todoweb/lists.html', {'lists' : lists})