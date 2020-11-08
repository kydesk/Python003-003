from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .models import Douban
from .models import Post
from .form import LoginForm

# Create your views here.

def index(request):
    comments = Douban.objects.all()
    return render(request, 'index.html', locals())

# 登录验证
def sign_in(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return redirect('/index')
            else:
                return HttpResponse('登录失败')

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'login.html', {'form': login_form})