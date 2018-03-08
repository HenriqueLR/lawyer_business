#coding: utf-8

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from main.models import OrderServiceModel, StatusModel
from main.form import OrderServiceForm
from main.utils import convert_string_to_date


def home(request):
    context = {}
    template_name = 'home.html'
    return render(request, template_name, context)



class OsAddView(CreateView):

    model = OrderServiceModel
    form_class = OrderServiceForm
    template_name = 'main/add_os.html'
    success_url = reverse_lazy('main:list_os')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Ordem de serviço criada com sucesso')
        return super().form_valid(form)



class OsListView(ListView):

    model = OrderServiceModel
    paginate_by = 10
    template_name = 'main/list_os.html'

    def get_queryset(self):
        qs = self.model.objects.all().order_by('-created_at')

        dt = self.request.GET.get('range_dt', '')
        if dt != '':
            dt_start, dt_end = dt.split('-')
            dt_start = convert_string_to_date(dt_start.strip()+' 00:00:00', '%d/%m/%Y %H:%M:%S')
            dt_end = convert_string_to_date(dt_end.strip()+' 23:59:59', '%d/%m/%Y %H:%M:%S')
            qs = qs.filter(created_at__gte=dt_start.strftime('%Y-%m-%d %H:%M:%S'),
                            created_at__lte=dt_end.strftime('%Y-%m-%d %H:%M:%S'))

        return qs



class OsDeleteView(DeleteView):

    model = OrderServiceModel
    template_name = 'main/os_confirm_delete.html'
    success_url = reverse_lazy('main:list_os')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, 'Lançamento de débito apagado com sucesso')
        return HttpResponseRedirect(self.success_url)



add_os = OsAddView.as_view()
list_os = OsListView.as_view()
delete_os = OsDeleteView.as_view()