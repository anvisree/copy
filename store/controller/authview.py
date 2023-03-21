from django.shortcuts import render,redirect
from django.contrib import messages
from store.forms import *

def register(request):
    form=CustomUserForm()
    if request.method == 'POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Register Successfully! Continue with Login')
            return redirect('/login')
    context={'form':form}
    return render(request,'store/auth/register.html',context)