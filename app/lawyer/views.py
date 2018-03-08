#coding: utf-8

from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from lawyer.models import LawyerModel
from main.models import OrderServiceModel, BusinessLawyerModel, StatusModel
from lawyer.form import LawyerForm
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



class OsListView(ListView):

    model = OrderServiceModel
    paginate_by = 10
    template_name = 'lawyer/business_lawyer.html'

    def get_queryset(self):
        qs = self.model.objects.all().filter(~Q(pk__in=BusinessLawyerModel.objects.all().filter(lawyer=3).values_list('order_service', flat=True))).order_by('-created_at')

        dt = self.request.GET.get('range_dt', '')
        if dt != '':
            dt_start, dt_end = dt.split('-')
            dt_start = convert_string_to_date(dt_start.strip()+' 00:00:00', '%d/%m/%Y %H:%M:%S')
            dt_end = convert_string_to_date(dt_end.strip()+' 23:59:59', '%d/%m/%Y %H:%M:%S')
            qs = qs.filter(created_at__gte=dt_start.strftime('%Y-%m-%d %H:%M:%S'),
                            created_at__lte=dt_end.strftime('%Y-%m-%d %H:%M:%S'))

        return qs



class OsListSignView(ListView):

    model = BusinessLawyerModel
    paginate_by = 10
    template_name = 'lawyer/list_os_sign.html'

    def get_context_data(self, **kwargs):
        context = super(OsListSignView, self).get_context_data(**kwargs)
        data = {
            'status_list': StatusModel.objects.all(),
        }
        context.update(data)
        return context

    def get_queryset(self):
        qs = self.model.objects.all().filter(lawyer=3).order_by('-created_at')

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



class SignOsAddView(CreateView):

    model = BusinessLawyerModel
    form_class = BusinessLawyerForm
    template_name = 'lawyer/sign_os.html'
    success_url = reverse_lazy('lawyer:list_os')

    def get_context_data(self, **kwargs):
        context = super(SignOsAddView, self).get_context_data(**kwargs)
        data = {
            'os': get_object_or_404(OrderServiceModel,
                    pk=self.kwargs['pk']),
            'lawyer': get_object_or_404(LawyerModel,
                    pk=3)
        }
        context.update(data)
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Ordem de serviço assinada com sucesso.')
        return super().form_valid(form)



list_os = OsListView.as_view()
sign_os = SignOsAddView.as_view()
list_os_sign = OsListSignView.as_view()