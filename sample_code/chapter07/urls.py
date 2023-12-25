from django.urls import path
from django.views.generic import TemplateView, FormView, RedirectView
from . import views

app_name = 'chapter07'

urlpatterns = [
    path('set_session/<str:param1>/', views.set_session, name='set_session'),
    path('view_session/', views.view_session, name='view_session'),
    path('get_session/', views.get_session, name='get_session'),
]
