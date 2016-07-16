from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html',{})

def login(request):
    return render(request,'login.html',{})

def sign_up(request):
    return render(request,'thanks-for-new-registration.html',{})

def create_notes(request):
    return render(request,'create-note.html',{})

def single_note(request):
    return render(request,'single-note.html',{})
