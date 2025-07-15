from django.shortcuts import render, redirect
from .forms import CreateUserForm

def register(request):
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = CreateUserForm()

    context = {
        'user_form': user_form
    }

    return render(request, 'register.html', context)

def login_user(request):
    return render(request, 'login.html')


