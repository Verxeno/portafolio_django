from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Portafolio
from .forms import PortaForm
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('portafolio')
        else:
            messages.info(request, 'Usuario o Contraseña incorrecto')
            return redirect('login')



    else:
        return render(request, 'paginas/login.html')

def registro(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'El usuario ya existe')
                return redirect(registro)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'El correo ya esta registrado')
                return redirect(registro)
            else:
                user = User.objects.create_user(username=username, password=password, 
                                        email=email, first_name=first_name, last_name=last_name)
                user.save()
                
                return redirect('login')


        else:
            messages.info(request, 'Las contraseñas no coinciden')
            return redirect(registro)
            

    else:
        return render(request, 'paginas/registro.html')

def logout_user(request):
    auth.logout(request)
    return redirect('login')

'''def registro(request):
    if request.method == 'GET':
        return render(request, 'paginas/registro.html',{'formreg': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                return redirect('login')
            except:
                return render(request, 'paginas/registro.html',{'formreg': UserCreationForm,'error': 'El usuario ya existe'})
        return render(request, 'paginas/registro.html',{'formreg': UserCreationForm,'error': 'Las contraseñas no coinciden'})'''

    

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def portafolio(request):
    portafolio=Portafolio.objects.all()
    return render(request, 'paginas/index.html',{'portafolio': portafolio})

def crear(request):
    formulario = PortaForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('portafolio')
    return render(request, 'paginas/crear.html', {'formulario': formulario})

def editar(request,id):
    portaup = Portafolio.objects.get(id=id)
    formularioup = PortaForm(request.POST or None, request.FILES or None, instance=portaup)
    if formularioup.is_valid() and request.POST:
        formularioup.save()
        return redirect('portafolio')

    return render(request, 'paginas/editar.html', {'formulario':formularioup})

def eliminar(request,id):
    portadelete = Portafolio.objects.get(id=id)
    portadelete.delete()
    return redirect('portafolio')
    

