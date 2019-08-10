from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from . import forms


@require_http_methods(['GET'])
def home_view(request):
    #View for Home page. Simply render the Home template.
    return render(request, 'notes/home.html')



@require_http_methods(['GET', 'POST'])
def signup_view(request):
    # If the User is already logged in, redirect to dashboard
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard:dashboard_page'))

    # GET request, render the page
    if request.method == 'GET':
        return render(request, 'notes/signup.html')

    # POST request, checks for errors and sign up
    else:
        signup_form = forms.SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.add_message(request, messages.SUCCESS, 'Success! Log in to continue...')
            return HttpResponseRedirect(reverse('dashboard:signin_page'))

        else:
            errors = signup_form.errors.as_text()
            if 'username' in errors:
                errors = errors.replace('username', 'mobile')
            messages.add_message(request, messages.ERROR, errors)
            return HttpResponseRedirect(reverse('dashboard:signup_page'))


@require_http_methods(['GET', 'POST'])
def signin_view(request):
    # If the User is already logged in, redirect to dashboard
    if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard:dashboard_page'))

    if request.method == 'GET':
        return render(request, 'notes/signin.html')

    else:
        signin_form = AuthenticationForm(request=request, data=request.POST)
        if signin_form.is_valid():
            django_login(request, signin_form.get_user())
            return HttpResponseRedirect(reverse('dashboard:dashboard_page'))

        else:
            errors = signin_form.errors.as_text()
            if 'username' in errors:
                errors = errors.replace('username', 'mobile')
            errors = errors.split('*')[2]
            messages.add_message(request, messages.ERROR, errors)
            return HttpResponseRedirect(reverse('dashboard:signin_page'))


@require_http_methods(['GET', 'POST'])
def dashboard_view(request):
    pass