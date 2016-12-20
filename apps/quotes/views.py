from django.shortcuts import render, redirect
from .models import Quotes
from ..regandlogin.models import User
from django.contrib import messages
# Create your views here.
def index(request):
    context ={
        'myquotes': Quotes.objects.filter(fave__id=request.session['user']),
        'otherquotes': Quotes.objects.exclude(fave__id=request.session['user']),
    }
    return render(request, 'quotes/index.html', context)

def create(request):
    if request.method == 'POST':
        errors = Quotes.objects.validate_quote(request.POST)
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('quotes:quotes_index')
        else:
            userobj = User.objects.get(id = request.session['user'])
            print userobj.name
            new_quote = Quotes.objects.create(text = request.POST['message'], author = request.POST['author'], user = userobj)
    return redirect('quotes:quotes_index')

def addfave(request, id):
    user = User.objects.get(id=request.session['user'])
    quote = Quotes.objects.get(id=id)
    quote.fave.add(user)
    quote.save()
    return redirect('quotes:quotes_index')

def removefave(request, id):
    user = User.objects.get(id=request.session['user'])
    quote = Quotes.objects.get(id=id)
    quote.fave.remove(user)
    quote.save()
    return redirect('quotes:quotes_index')

def user(request, id):
    context={
        'users': User.objects.get(id=id),
        'quotesmade': Quotes.objects.filter(user__id=id)
    }
    return render(request, 'quotes/users.html', context)
