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
from accounts.form import UserForm



class BusinessAddView(CreateView):

    model = BusinessModel
    form_class = BusinessForm
    template_name = 'business/add_business.html'
    success_url = reverse_lazy('business:add_business')

    def get_context_data(self, **kwargs):
        context = super(BusinessAddView, self).get_context_data(**kwargs)
        data = {
            'user_form':UserForm(self.request.POST or None)
        }
        context.update(data)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']
        if user_form.is_valid() and form.is_valid():
            user = user_form.save()
            form.save(user=user)
        messages.success(self.request, 'Empresa criada com sucesso')
        return super().form_valid(form)



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



add_business = BusinessAddView.as_view()
list_os_validate = OsValidateListView.as_view()