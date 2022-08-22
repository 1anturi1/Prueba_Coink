from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.urls import reverse

# Create your views here.


def index(request):
    return render(request, "index.html")


def listUsers(request):
    queryset = User.objects.all()
    context = {
        'users_list': queryset
    }
    return render(request, "listUsers.html", context)

@csrf_exempt
def addUser(request):    
    if request.method == 'POST':
        form = UserForm(request.POST)       
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Usuario creado satisfactoriamente')
        else:
            print(form.errors.items)
            context = {
                'form': form,
            }
            messages.add_message(request, messages.ERROR,'El usuario no ha podido ser creado')            
    return render(request, "addUser.html")
