from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

def registro(request):
  if request.method == 'GET':
    context = {
    'titulo':'Registro',
    'form':UserCreationForm
  }
    return render(request, 'registro.html',context)
  elif request.method == 'POST':
      if request.POST['password1']==request.POST['password2']:
        try:
          user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
          user.save()
          login(request,user)
          return redirect('principal')
        except:
          context = {
        'form':UserCreationForm,
        'error':'El usuario ya existe'
      }
      return render(request, 'registro.html',context)
      
def iniciosesion(request):
  if request.method=='GET':
    context={
    'titulo':'Iniciar Sesión',
    'form':AuthenticationForm
  }
    return render(request,'iniciosesion.html',context)
  else:
    user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
    if user==None:
      context={
        'error':'Usuario o contraseña incorrectos',
        'form':AuthenticationForm
      }
      return render(request, 'iniciosesion.html',context)
    else:
      login(request,user)
      return redirect('principal')

def principal(request):
  context={
    'titulo':'Principal'
  }
  return render(request,'principal.html',context)

@login_required
def cerrarsesion(request):
  logout(request)
  return redirect('principal')