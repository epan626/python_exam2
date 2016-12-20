from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
    return render(request, 'regandlogin/index.html')

def register(request):
    if request.method == 'POST':
        print 'yes'
        errors = User.objects.validate_registration(request.POST)
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('rnl:rnl_index')
        else:
            if User.objects.register(request.POST):
                messages.success(request, 'You have successfully created an account, please login to continue')
            else:
                messages.error(request, 'Something went wrong')
    return redirect(reverse('rnl:rnl_index'))

def login(request):
    if request.method != 'POST':
        return redirect('rnl:rnl_index')
    user = User.objects.check_login(request.POST)
    if user:
        request.session['user'] = user.id
        request.session['name'] = user.name
        print 'hello'
        return redirect('quotes:quotes_index')
    else:
        messages.error(request, 'Invalid login credentials')
        return redirect(reverse('rnl:rnl_index'))

def logout(request):
    request.session.pop('user')
    messages.success(request, 'Successful logged out')
    return redirect(reverse('rnl:rnl_index'))
