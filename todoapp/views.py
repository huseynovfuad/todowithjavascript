from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoCreateForm,TodoUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
# Create your views here.

@login_required
def home(request):
    create_form = TodoCreateForm()
    update_form = TodoUpdateForm()
    todo_list = Todo.objects.filter(author = request.user).order_by("-created_at")
    context = {'todo_list':todo_list,'create_form':create_form,'update_form':update_form}
    return render(request,'todo/home.html',context)


def create(request):
    text1 = request.GET.get('text')
    obj = Todo.objects.create(text = text1,author=request.user)
    info = {"id":obj.id,"text":obj.text}
    data = {"info":info}
    return JsonResponse(data)


def delete(request):
    id1 = request.GET.get('id',None)
    Todo.objects.get(id=id1).delete()
    data = {
        'deleted': True
    }
    return JsonResponse(data)


def update(request):
    id1 = request.GET.get('id', None)
    text1 = request.GET.get('text', None)
    obj = Todo.objects.get(id=id1)
    obj.text = text1
    obj.save()
    info = {'id':obj.id,'text':obj.text}
    data = {
            'info': info
    }
    return JsonResponse(data)