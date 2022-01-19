#coding: utf-8

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from main.models import OrderServiceModel, StatusModel
from main.form import OrderServiceForm
from main.permissions import PermissionsMainMixin, PermissionsMainDeleteOsMixin
from main.decorators import user_check



@login_required
@user_check
def home(request):
    context = {}
    template_name = 'home.html'
    return render(request, template_name, context)



class OsAddView(PermissionsMainMixin, CreateView):

    model = OrderServiceModel
    form_class = OrderServiceForm
    template_name = 'main/add_os.html'
    success_url = reverse_lazy('main:list_os')
    message_success = 'Ordem de serviço criada'



class OsListView(PermissionsMainMixin, ListView):

    model = OrderServiceModel
    paginate_by = 10
    template_name = 'main/list_os.html'



class OsDeleteView(PermissionsMainDeleteOsMixin, DeleteView):

    model = OrderServiceModel
    template_name = 'main/os_confirm_delete.html'
    success_url = reverse_lazy('main:list_os')
    message_success = 'Ordem de serviço apagada'



add_os = OsAddView.as_view()
list_os = OsListView.as_view()
delete_os = OsDeleteView.as_view()