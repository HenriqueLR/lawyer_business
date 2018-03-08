#coding: utf-8

from django.template import Library

register = Library()


@register.filter(name='addcss')
def addcss(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name='placeholder')
def placeholder(value, arg):
    value.field.widget.attrs["placeholder"] = arg
    return value

@register.filter(name='textarea')
def textarea(value, arg):
    value.field.widget.attrs["rows"] = arg
    return value

@register.filter(name='real_br_money_mask')
def real_br_money_mask(my_value):
    a = '{:,.2f}'.format(float(my_value))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')