from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm,CreateUserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        form= ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request,('Item has been added to list!'))
            return render(request, 'home.html',{'all_items':all_items})
    else:
        all_items = List.objects.all
        return render(request,"home.html",{'all_items':all_items})

@login_required(login_url='login')
def delete(request, List_id):
    item = List.objects.get(pk=List_id)     
    item.delete()
    messages.success(request, ('Item has been deleted!'))   
    return redirect('home')

@login_required(login_url='login')    
def cross_off(request, List_id):
    item = List.objects.get(pk=List_id)     
    item.completed = True
    item.save()
    return redirect('home')

@login_required(login_url='login')
def uncross(request, List_id):
    item = List.objects.get(pk=List_id)     
    item.completed = False
    item.save()  
    return redirect('home')

@login_required(login_url='login')
def edit(request,List_id):
    if request.method == 'POST':
        item=List.objects.get(pk=List_id)
        form= ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request,('Item has been added to list!'))
            return redirect('home')
    else:
        item = List.objects.get(pk=List_id)
        return render(request,'edit.html',{'item':item})