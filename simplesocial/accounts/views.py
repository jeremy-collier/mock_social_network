from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

# Create your views here.
class SignUp(CreateView):
    #sets and displays a instance of the UserCreateForm for user to fill out
    form_class = forms.UserCreateForm
    #reverse_lazy redirects user after they have submitted the above form
    #redirects them to the url named login
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
