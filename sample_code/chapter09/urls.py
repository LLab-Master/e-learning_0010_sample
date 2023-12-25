from django.urls import path
from django.views.generic import TemplateView, FormView, RedirectView
from . import views

app_name = 'chapter09'

urlpatterns = [
    path('', views.app_top, name='app_top'),
    path('home/', TemplateView.as_view(template_name='app_top.html'), name='home'),
    path('add/', views.insert_product_end, name='add'),
]
