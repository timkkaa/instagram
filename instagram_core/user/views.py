from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from user.models import User


class MakeLoginView(View):

    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        if not username or not password:
            print(username, password)
            return render(request, 'login.html', {'error': 'Пожалуйста, заполните оба поля'})

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            context = {
                'current_user': request.user
            }
            print('Login successful')
            return render(request, 'home.html', context)
        else:
            return render(request, 'login.html', {'error': 'Неверное имя пользователя или пароль'})


class LoginView(TemplateView):
    template_name = 'login.html'



class MakeRegistrationView(TemplateView):
    template_name = 'sign_up.html'
    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('name')
        lastname = self.request.POST.get('lastname')
        firstname = self.request.POST.get('firstname')
        password = self.request.POST.get('password')

        if not   username or not lastname or not firstname or not password:
            print(username, lastname, firstname, password)
            render(request, template_name='sign_up.html')

        user = User(username=username, lastname=lastname, firstname=firstname)
        user.password = make_password(password=password)

        try:
            user.save()
        except:
            return render(request, template_name='login.html', context={'current_user': self.request.user})
        login(self.request, user)
        context = {
            'current_user': self.request.user
        }

        return render(request, template_name='login.html', context=context)

class RegistrationView(TemplateView):
    template_name = 'sign_up.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'