from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            success = True
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                success = False
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is taken')
                success = False
            if success:
                # Register successfully
                user = User.objects.create_user(
                    username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(
                    request, 'Register successfully, please login')
                return redirect('login')
            else:
                # Failed
                return redirect('register')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    return render(request, 'accounts/register.html')


def dashboard(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        contacts = Contact.objects.filter(user_id=user_id)
        return render(request, 'accounts/dashboard.html', {'contacts': contacts})
    else:
        messages.error(request, 'Please login')
        return redirect('login')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged out successfully')
    return redirect('index')
