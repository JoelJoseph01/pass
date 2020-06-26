from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'pgen/home.html',{'password':'sgdjg468egs' })

def password(request):

    characters = list('abcdefghijklmnopqrstuvuxyz')

    length = int(request.GET.get('length',12))

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    if request.GET.get('numbers'):
        characters.extend('1234567890')
    
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()>')


    thepassword= ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'pgen/password.html', {'password':thepassword})

def about(request):
     return render(request,'pgen/about.html')