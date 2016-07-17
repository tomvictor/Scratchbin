from django.shortcuts import render
from .forms import NewNoteForm
# Create your views here.

def home(request):
    return render(request,'home.html',{})

def login(request):
    return render(request,'login.html',{})

def sign_up(request):
    return render(request,'thanks-for-new-registration.html',{})

def create_notes(request):
    form = NewNoteForm()
    return render(request,'create-note.html',{'form': form})

def single_note(request):
    return render(request,'single-note.html',{})
