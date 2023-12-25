from django.urls import path
from . import views # アプリの views を import
from django.views import generic # genericを import

app_name = 'chapter02'   # アプリの逆引き名

urlpatterns = [
    path('hello/',          # URL
        views.hello_django, # View関数名
        name='hello1'),     # 逆引き名

    path('welcome/',
        views.welcome_page,
        name='welcome1'),

    path('redirect/',
        views.redirect_to_welcome,
        name='welcome_redirect'),

    path('welcome_class/',
        views.WelcomeTemplateView.as_view(), # as_view メソッド
        name='welcome_class'),

    path('welcome_class2/',
        generic.TemplateView.as_view(template_name='welcome.html'), 
        name='welcome_class2'),
]
