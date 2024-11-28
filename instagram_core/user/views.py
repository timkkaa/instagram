from sqlite3 import IntegrityError

from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect


from .models import User


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
        username = request.POST.get('user_name')
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        password = request.POST.get('password')
        if not username or not firstname or not lastname or not password:
            return render(request, self.template_name, {'error': 'Все поля обязательны для заполнения'})
        if User.objects.filter(user_name=username).exists():
            return render(request, self.template_name, {'error': 'Такой пользователь уже существует'})
        hashed_password = make_password(password)
        user = User(user_name=username, first_name=firstname, last_name=lastname, password=hashed_password)

        try:
            user.save()
        except Exception as e:
            return render(request, self.template_name, {'error': f'Ошибка при создании пользователя: {e}'})

        login(request, user)

        return redirect('login-url')

class RegistrationView(TemplateView):
    template_name = 'sign_up.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'