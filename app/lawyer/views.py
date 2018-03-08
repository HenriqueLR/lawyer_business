#coding: utf-8

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from lawyer.models import LawyerModel
from lawyer.form import LawyerForm



class LawyerAddView(CreateView):

    model = LawyerModel
    form_class = LawyerForm
    template_name = 'lawyer/add_lawyer.html'
    success_url = reverse_lazy('lawyer:add_lawyer')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Advogado criado com sucesso')
        return super().form_valid(form)



add_lawyer = LawyerAddView.as_view()