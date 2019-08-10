from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from . import forms


@require_http_methods(['GET'])
def home_view(request):
    #View for Home page. Simply render the Home template.
    return render(request, 'notes/home.html')



@require_http_methods(['GET', 'POST'])
def signup_view(request):
    # GET request, render the page
    if request.method == 'GET':
        return render(request, 'notes/signup.html')

    # POST request, checks for errors and sign up
    else:
        signup_form = forms.SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.add_message(request, messages.SUCCESS, 'Success! Log in to continue...')

        else:
            errors = signup_form.errors.as_text()
            if 'username' in errors:
                errors = errors.replace('username', 'mobile')
            messages.add_message(request, messages.ERROR, errors)
            return HttpResponseRedirect(reverse('dashboard:signup_page'))


@require_http_methods(['GET', 'POST'])
def signin_view(request):
    if request.method == 'GET':
        return render(request, 'notes/signin.html')

    else:
        pass