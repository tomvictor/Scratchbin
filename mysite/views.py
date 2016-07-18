from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import Http404
from .forms import NoteForm,LoginForm,SignUpForm
from .models import notes
from django.utils import timezone


# Create your views here.

def home(request):
    if request.user.is_authenticated():
        all_notes = notes.objects.order_by('published_date')
        query = request.GET.get("q")
        if query:
            all_notes = notes.objects.filter(title__icontains=query)

        return render(request, 'home.html', {'notes': all_notes})
    else:
        return redirect("mysite:login-page")

        # return render(request,'home.html',{'notes':all_notes})


def login(request):
    form = LoginForm(request.POST or None)
    signup_form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        #print(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    messages.success(request, "You have been securely logged in")
                    return redirect("mysite:home-page")
                else:
                    messages.success(request, "The password is valid, but the account has been disabled!")
                    return redirect("mysite:login-page")
            else:
                #print("The username and password were incorrect.")
                messages.success(request, "The username and password were incorrect.")
                return redirect("mysite:login-page")
        else:
            messages.success(request, "The username and password were invalid.")
            return redirect("mysite:login-page")

    context={"Form":form,"SignUpForm":signup_form
    }
    return render(request, 'login.html', context)


def sign_up(request):
    if request.method == 'POST':
        form= SignUpForm(request.POST )
        #print(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            #gender = form.cleaned_data.get("gender")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.date_joined = timezone.now()
            user.save()
            messages.success(request, "Hi,%s ! You have been Succesfully Signed Up, Please Login Again " %(first_name))
    return render(request, 'thanks-for-new-registration.html', {})

def logout_view(request):
    logout(request)
    messages.success(request, "you have been logged out Succesfully")
    return HttpResponseRedirect('/login/')

def note_detail(request, id=None):
    if not request.user.is_authenticated():
        raise Http404
    current_note = get_object_or_404(notes, id=id)
    return render(request, 'single-note.html', {'this_note': current_note})

def create_notes(request):
    if not request.user.is_authenticated():
        raise Http404
    form = NoteForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        print(instance.author)
        print(form.cleaned_data.get("title"))
        instance.save()
        messages.success(request, "Succesfully created new note")
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, 'note-form.html', {'form': form})


def update_notes(request, id=None):
    if not request.user.is_authenticated():
        raise Http404
    instance = get_object_or_404(notes, id=id)
    form = NoteForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.last_update_date = timezone.now()
        instance.save()
        messages.success(request, "Succesfully Updated your note")
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, 'note-form.html', {'form': form})


def delete_notes(request, id=None):
    if not request.user.is_authenticated():
        raise Http404
    instance = get_object_or_404(notes, id=id)
    instance.delete()
    messages.success(request, "Succesfully deleted your note")
    return redirect("mysite:home-page")


def scrum(request):
    if not request.user.is_authenticated():
        raise Http404
    return render(request, 'scrum.html', {})

def about(request):
    messages.success(request, "The Sticknote is a modified version of bin.technorip.com. Currently in beta testing. "
                              " Give your valuable feedbacks")
    return render(request,'about.html',{})
