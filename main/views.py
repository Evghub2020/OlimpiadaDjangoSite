from django.shortcuts import render, redirect
from .models import Employees
from .forms import ParticipantsForm

def index(request):
    emp = Employees.objects.all()
    return render(request,'main/index.html', {'emp': emp})

def registration(request):
    error = ''
    
    if request.method == 'POST':
        form = ParticipantsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = ParticipantsForm()
    return render(request, 'main/registration.html', {'form': form})


