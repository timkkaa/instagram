from django.shortcuts import render

from django.views.generic import TemplateView, View


class LoginView(View):
    template_name = 'login.html'

class RegistrationView(View):
    template_name = 'sign_up.html'