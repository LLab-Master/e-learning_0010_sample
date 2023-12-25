from django.urls import path
from django.views.generic import TemplateView, FormView, RedirectView
from django.contrib.auth.forms import UserCreationForm
from . import views

app_name = 'chapter10'

urlpatterns = [
    path('bs5/', FormView.as_view(
                    template_name='bs5_sample.html',
                    form_class=UserCreationForm),
         name='bs5_sample'),
]
