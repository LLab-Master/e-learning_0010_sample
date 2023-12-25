from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from .models import Product


class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True


class MyLogoutView(LogoutView):
    pass


class MyLogoutOKView(TemplateView):
    template_name = 'logout.html'


def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()  # ログイン対象の user (Userクラス)
            if user:
                login(request, user)    # ログイン
                return redirect('../login_ok/')  # ログイン完了ページへリダイレクト
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def login_ok(request):
    return render(request, 'login_ok.html')


def my_logout(request):
    logout(request)
    return render(request, 'logout.html')


@login_required
def member_only(request):
    return render(request, 'member_only.html')


class MemberOnlyView(LoginRequiredMixin, TemplateView):
    template_name = 'member_only.html'


@permission_required('chapter08.view_product')
def grpA(request):
    products = Product.objects.all()
    return render(request, 'grpA.html', {'products': products})


class GrpBView(PermissionRequiredMixin, ListView):
    template_name = 'grpB.html'
    model = Product
    permission_required = 'chapter08.view_product'


def add_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../add_user_ok/')
    else:
        form = UserCreationForm()

    return render(request, 'add_user.html', {'form':form})

class AddUserView(CreateView):
    template_name = 'add_user.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('chapter08:add_user_ok')
