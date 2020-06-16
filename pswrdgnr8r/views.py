from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'pswrdgnr8r/home.html', {'password': 'raddahRaddahRaaaahhddd'})

def password(request):
    thePassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('passwordlength'))
    if request.GET.get('upperCase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specialCharacters'):
        characters.extend(list('~`!@#$%^&*()_-=+}]{[\|/?'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))


    for x in range(length):
        thePassword += random.choice(characters)
    return render(request, 'pswrdgnr8r/password.html', {'password': thePassword})

