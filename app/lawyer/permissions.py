#coding: utf-8

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.http import Http404
from lawyer.models import LawyerModel
from main.models import StatusModel, BusinessLawyerModel, OrderServiceModel
from main.utils import convert_string_to_date
from django.contrib import messages



class PermissionsGeralMixin(object):

    @classmethod
    def as_view(cls):
        return login_required(super(PermissionsGeralMixin, cls).as_view())

    @method_decorator(never_cache)
    @method_decorator(user_passes_test(lambda u: u.is_active,login_url='accounts:logout'))
    def dispatch(self, request, *args, **kwargs):
        self.lawyer = LawyerModel.objects.filter(user=self.request.user)
        if not self.lawyer.exists():
            return redirect('accounts:logout')
        return super(PermissionsGeralMixin, self).dispatch(request, *args, **kwargs)



class PermissionsLawyerListMixin(PermissionsGeralMixin):

    def get_queryset(self):
        qs = self.model.objects.all() \
            .filter(~Q(pk__in=BusinessLawyerModel.objects.all() \
                        .filter(lawyer=self.lawyer.get()).values_list('order_service', flat=True))) \
            .filter(~Q(pk__in=BusinessLawyerModel.objects.all() \
                        .filter(status__name='delegada') \
                        .filter(status__name='finalizada').values_list('status', flat=True))) \
            .order_by('-created_at')

        dt = self.request.GET.get('range_dt', '')
        if dt != '':
            dt_start, dt_end = dt.split('-')
            dt_start = convert_string_to_date(dt_start.strip()+' 00:00:00', '%d/%m/%Y %H:%M:%S')
            dt_end = convert_string_to_date(dt_end.strip()+' 23:59:59', '%d/%m/%Y %H:%M:%S')
            qs = qs.filter(created_at__gte=dt_start.strftime('%Y-%m-%d %H:%M:%S'),
                            created_at__lte=dt_end.strftime('%Y-%m-%d %H:%M:%S'))

        return qs



class PermissionsLawyerListSignOsMixin(PermissionsGeralMixin):

    def get_context_data(self, **kwargs):
        context = super(PermissionsLawyerListSignOsMixin, self).get_context_data(**kwargs)
        data = {
            'status_list': StatusModel.objects.all(),
        }
        context.update(data)
        return context

    def get_queryset(self):
        qs = self.model.objects.filter_lawyer(self.lawyer.get()).order_by('-created_at')

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



class PermissionsLawyerSignOsMixin(PermissionsGeralMixin):

    def get_context_data(self, **kwargs):
        context = super(PermissionsLawyerSignOsMixin, self).get_context_data(**kwargs)
        data = {
            'os': get_object_or_404(OrderServiceModel,
                    pk=self.kwargs['pk']),
        }
        context.update(data)
        return context

    def form_valid(self, form):
        form.instance.lawyer = self.lawyer.get()
        form.instance.status = StatusModel.objects.get(name='criada')
        messages.success(self.request, 'Ordem de serviço assinada com sucesso')
        return super(PermissionsLawyerSignOsMixin, self).form_valid(form)