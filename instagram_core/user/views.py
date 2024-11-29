from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect

from user.models import CustomUser



class MakeLoginView(View):

    def post(self, request, *args, **kwargs):
        data = request.POST
        username = data.get('name')
        password = data.get('password')

        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return redirect('login-url')

        if user.check_password(password):
            login(request, user)
            return redirect('home-url')

        else:
            return render('login-url')

class LoginView(TemplateView):
    template_name = 'login.html'


class MakeRegistrationView(TemplateView):
    template_name = 'sign_up.html'

    def post(self, request, *args, **kwargs):
        data = request.POST
        username = data.get('name')
        lastname = data.get('lastname')
        firstname = data.get('firstname')
        password = data.get('password')

        user = CustomUser(username=username, last_name=lastname, first_name=firstname)
        user.password = make_password(password=password)

        try:
            user.save()
        except:
            return render(request, template_name='login.html', context={'user': self.request.user})
        login(self.request, user)
        context = {
            'user': self.request.user
        }

        return render(request, template_name='profile.html', context=context)


class RegistrationView(TemplateView):
    template_name = 'sign_up.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'

class HomeView(TemplateView):
    template_name = 'home.html'