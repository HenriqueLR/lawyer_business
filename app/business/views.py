#coding: utf-8

from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from business.models import BusinessModel
from business.form import BusinessForm
from main.models import BusinessLawyerModel, StatusModel, OrderServiceModel
from main.utils import convert_string_to_date
from accounts.form import UserCreateForm
from business.permissions import PermissionsBusinessMixin



def add_business(request):
    template_name = 'business/add_business.html'
    user_form = UserCreateForm(request.POST or None)
    business_form = BusinessForm(request.POST or None)

    if user_form.is_valid() and business_form.is_valid():
        user = user_form.save()
        business = business_form.save(user=user)
        messages.success(request, 'Empresa criada com sucesso')
        return HttpResponseRedirect(reverse_lazy('accounts:login'))

    context = {
        'user_form':user_form,
        'business_form':business_form
    }
    return render(request, template_name, context)



class OsValidateListView(PermissionsBusinessMixin, ListView):

    model = BusinessLawyerModel
    paginate_by = 10
    template_name = 'business/list_os_validate.html'



@login_required
def update_status_os(request, *args, **kwargs):
    business = get_object_or_404(BusinessModel, user=request.user)
    os_datail = get_object_or_404(BusinessLawyerModel, pk=kwargs['pk'], order_service__business=business)
    os_datail.status = get_object_or_404(StatusModel, name=kwargs['key'])
    os_datail.save()
    return HttpResponseRedirect(reverse_lazy('business:list_os_validate'))



list_os_validate = OsValidateListView.as_view()