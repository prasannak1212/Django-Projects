from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
# from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Record

def home(request):
    return render(request, 'home.html')

@login_required(login_url='my-login')
def dashboard(request):
    my_records = Record.objects.all()
    context = {'records':my_records}
    return render(request, 'dashboard.html', context=context)

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
    context = {'form': form}
    return render(request, 'register.html', context=context)

def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')

    context = {'form2':form}

    return render(request, 'my-login.html', context=context)

def user_logout(request):
    logout(request)
    return redirect('my-login')

@login_required(login_url='my-login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form':form}

    return render(request, 'create-records.html', context=context)

@login_required(login_url='my-login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form':form}
    return render(request, 'update-records.html', context=context)

@login_required(login_url='my-login')
def view_record(request, pk):
    all_records = Record.objects.get(id=pk)
    context = {'record':all_records}
    return render(request, 'view-records.html', context=context)

@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    return redirect('dashboard')