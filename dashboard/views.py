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

        else:
            errors = signup_form.errors
            error_message = ''
            for k in errors:
                error_message = error_message + f'{k} - {errors[k]}. '
            messages.add_message(request, messages.ERROR, error_message)
            return HttpResponseRedirect('dashboard:signup_page')


