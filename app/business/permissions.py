#coding: utf-8

from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.http import Http404
from business.models import BusinessModel
from main.models import StatusModel
from main.utils import convert_string_to_date
from django.contrib import messages



class PermissionsGeralMixin(object):

    @classmethod
    def as_view(cls):
        return login_required(super(PermissionsGeralMixin, cls).as_view())

    @method_decorator(never_cache)
    @method_decorator(user_passes_test(lambda u: u.is_active,login_url='accounts:logout'))
    def dispatch(self, request, *args, **kwargs):
        self.business = BusinessModel.objects.filter(user=self.request.user)
        if not self.business.exists():
            return redirect('accounts:logout')
        return super(PermissionsGeralMixin, self).dispatch(request, *args, **kwargs)



class PermissionsBusinessMixin(PermissionsGeralMixin):

    def get_context_data(self, **kwargs):
        context = super(PermissionsBusinessMixin, self).get_context_data(**kwargs)
        data = {
            'status_list': StatusModel.objects.all(),
        }
        context.update(data)
        return context

    def get_queryset(self):
        qs = self.model.objects.filter_user(self.business.get()).order_by('-created_at')

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