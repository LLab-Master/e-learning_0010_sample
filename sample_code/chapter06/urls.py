from django.urls import path
from django.views.generic import TemplateView, FormView, RedirectView
from . import views

app_name = 'chapter06'

urlpatterns = [
    path('template1/', views.MyTemplateView.as_view(), name='template1'),
    path('template2/', TemplateView.as_view(template_name='template1.html'), name='my_template2'),

    path('form1/', views.MyFormView.as_view(), name='form1'),
    path('form1_success/', TemplateView.as_view(template_name='form1_success.html'),
                                               name='form_success'),

    path('redirect1/', views.MyRedirectView.as_view(), name='redirect1'),
    path('redirect2/', RedirectView.as_view(url='https://www.google.com/'),
                                               name='redirect2'),

    path('member_create/', views.MemberCreateView.as_view(), name='member_create'),
    path('member_create_end/', views.MemberCreateEndView.as_view(), name='member_create_end'),

    path('member_list/', views.MemberListView.as_view(), name='member_list'),

    path('member_detail/<str:pk>/', views.MemberDetailView.as_view(), name='member_detail'),

    path('member_update/<str:pk>/', views.MemberUpdateView.as_view(), name='member_update'),
    path('member_update_end/', views.MemberUpdateEndView.as_view(), name='member_update_end'),

    path('member_delete/<str:pk>/', views.MemberDeleteView.as_view(), name='member_delete'),
    path('member_delete_end/', views.MemberDeleteEndView.as_view(), name='member_delete_end'),
]
