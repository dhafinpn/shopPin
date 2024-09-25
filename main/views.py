from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render, redirect 
from main.forms import ReviewEntryForm
from main.models import ReviewEntry
from django.http import HttpResponse
from django.core import serializers
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login')

def show_main(request):
    review_entries = ReviewEntry.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'product' : 'Manchester United 2024/2025 Official Jersey',
        'price': '2000000',
        'description': 'The Official Jersey of Manchester United for 2024/2025 season',
        'review_entries': review_entries,
        'last_login': request.COOKIES['last_login'], 
        }

    return render(request, "main.html", context)

def create_review_entry(request):
    form = ReviewEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        review_entry = form.save(commit=False)
        review_entry.user = request.user
        review_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_review_entry.html", context)

def show_xml(request):
    data = ReviewEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ReviewEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ReviewEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ReviewEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response