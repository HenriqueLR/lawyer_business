#coding: utf-8

from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from business.models import BusinessModel
from business.form import BusinessForm
from main.models import BusinessLawyerModel, StatusModel, OrderServiceModel
from main.utils import convert_string_to_date
from accounts.form import UserCreateForm



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



class OsValidateListView(ListView):

    model = BusinessLawyerModel
    paginate_by = 10
    template_name = 'business/list_os_validate.html'

    def get_context_data(self, **kwargs):
        context = super(OsValidateListView, self).get_context_data(**kwargs)
        data = {
            'status_list': StatusModel.objects.all(),
        }
        context.update(data)
        return context

    def get_queryset(self):
        qs = self.model.objects.all().filter(order_service__business=1).order_by('-created_at')

        status = self.request.GET.get('status', '').lower()
        if status != '' and status != 'todos':
            qs = qs.filter(status__name=status)

        dt = self.request.GET.get('range_dt', '')
        if dt != '':
            dt_start, dt_end = dt.split('-')
            dt_start = convert_string_to_date(dt_start.strip()+' 00:00:00', '%d/%m/%Y %H:%M:%S')
            dt_end = convert_string_to_date(dt_end.strip()+' 23:59:59', '%d/%m/%Y %H:%M:%S')
            qs = qs.filter(created_at__gte=dt_start.strftime('%Y-%m-%d %H:%M:%S'),
                            created_at__lte=dt_end.strftime('%Y-%m-%d %H:%M:%S'))

        return qs



def update_status_os(request, *args, **kwargs):
    os_datail = get_object_or_404(BusinessLawyerModel, pk=kwargs['pk'])
    os_datail.status = get_object_or_404(StatusModel, name=kwargs['key'])
    os_datail.save()
    return HttpResponseRedirect(reverse_lazy('business:list_os_validate'))



list_os_validate = OsValidateListView.as_view()