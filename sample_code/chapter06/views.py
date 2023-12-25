from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from chapter05.models import Product

from .models import Member
from .forms import MyForm

class MyTemplateView(generic.TemplateView):
    template_name = 'template1.html'

class MyFormView(generic.FormView):
    template_name = 'form1.html'
    form_class = MyForm
    success_url = reverse_lazy('chapter06:form_success')


class MyRedirectView(generic.RedirectView):
    url = 'https://www.google.com/'

class MemberCreateView(generic.CreateView):
    template_name = 'member_create.html'
    model = Member
    fields = '__all__'
    success_url = reverse_lazy('chapter06:member_create_end')

class MemberCreateEndView(generic.TemplateView):
    template_name = 'member_create_end.html'

class MemberListView(generic.ListView):
    template_name = 'member_list.html'
    model = Member

class MemberDetailView(generic.DetailView):
    template_name = 'member_detail.html'
    model = Member

class MemberUpdateView(generic.UpdateView):
    template_name = 'member_update.html'
    model = Member
    # queryset = Member.objects.filter(id__contains="1")
    fields = '__all__'
    success_url = reverse_lazy('chapter06:member_update_end')

class MemberUpdateEndView(generic.TemplateView):
    template_name = 'member_update_end.html'

class MemberDeleteView(generic.DeleteView):
    template_name = 'member_delete.html'
    model = Member
    success_url = reverse_lazy('chapter06:member_delete_end')

class MemberDeleteEndView(generic.TemplateView):
    template_name = 'member_delete_end.html'
