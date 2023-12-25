from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import generic

def hello_django(request):
    return HttpResponse('<h1>Hello Django!</h1>')


def welcome_page(request):
    return render(request, 'welcome.html')


def redirect_to_welcome(request):
    return redirect('chapter02:welcome1')   # app_name:逆引き名
    # return redirect('/chapter02/welcome')  # URL(app名から)
    # return redirect('../welcome')          # URL(相対パス指定)


class WelcomeTemplateView(generic.TemplateView):
    template_name = 'welcome.html'
