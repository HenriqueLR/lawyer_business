#coding: utf-8

from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from lawyer.models import LawyerModel
from main.models import OrderServiceModel, BusinessLawyerModel, StatusModel
from lawyer.form import LawyerForm
from lawyer.permissions import PermissionsLawyerListMixin, PermissionsLawyerListSignOsMixin, PermissionsLawyerSignOsMixin
from main.form import BusinessLawyerForm
from main.utils import convert_string_to_date
from accounts.form import UserCreateForm



def add_lawyer(request):
    template_name = 'lawyer/add_lawyer.html'
    user_form = UserCreateForm(request.POST or None)
    lawyer_form = LawyerForm(request.POST or None)

    if user_form.is_valid() and lawyer_form.is_valid():
        user = user_form.save()
        lawyer = lawyer_form.save(user=user)
        messages.success(request, 'Advogado criado com sucesso')
        return HttpResponseRedirect(reverse_lazy('accounts:login'))

    context = {
        'user_form':user_form,
        'lawyer_form':lawyer_form
    }
    return render(request, template_name, context)



class OsListView(PermissionsLawyerListMixin, ListView):

    model = OrderServiceModel
    paginate_by = 10
    template_name = 'lawyer/business_lawyer.html'



class OsListSignView(PermissionsLawyerListSignOsMixin, ListView):

    model = BusinessLawyerModel
    paginate_by = 10
    template_name = 'lawyer/list_os_sign.html'



class SignOsAddView(PermissionsLawyerSignOsMixin, CreateView):

    model = BusinessLawyerModel
    form_class = BusinessLawyerForm
    template_name = 'lawyer/sign_os.html'
    success_url = reverse_lazy('lawyer:list_os')



list_os = OsListView.as_view()
sign_os = SignOsAddView.as_view()
list_os_sign = OsListSignView.as_view()