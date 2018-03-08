#coding: utf-8

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from business.models import BusinessModel
from business.form import BusinessForm



class BusinessAddView(CreateView):

    model = BusinessModel
    form_class = BusinessForm
    template_name = 'business/add_business.html'
    success_url = reverse_lazy('business:add_business')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Empresa criada com sucesso')
        return super().form_valid(form)



add_business = BusinessAddView.as_view()