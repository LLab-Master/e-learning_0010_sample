from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'chapter08'

urlpatterns = [
    path('login_cls/',
        LoginView.as_view(
            template_name = 'login.html',
            redirect_authenticated_user = True),
        name='login_cls'),
    path('logout_cls/', LogoutView.as_view(), name='logout'),
    path('logout_ok/',
        TemplateView.as_view(
            template_name = 'logout.html'
        ), name='logout_ok'),

    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('login_ok/', views.login_ok, name='login_ok'),
    path('member_only/', views.member_only, name='member_only'),
    path('member_only_cls/', views.MemberOnlyView.as_view(), name='member_only2'),
    path('grpA/', views.grpA, name='grpA'),
    path('grpB/', views.GrpBView.as_view(), name='grpB'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_user_ok/', TemplateView.as_view(template_name='add_user_ok.html'), name='add_user_ok'),
    path('add_user_cls/', views.AddUserView.as_view(), name='add_user2'),
    
]
