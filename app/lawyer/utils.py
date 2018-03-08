#coding: utf-8

import re
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError



error_messages = {
    'invalid': "Numero de cpf inválido.",
    'digits_only': "Somente numeros são possiveis.",
    'max_digits': "É obrigatório 11 digitos.",
    'invalid_phone': 'Entre com número de telefone válido ex: XX-XXXXX-XXXX',
    'len_phone': 'Tamanhos permitidos XX-XXXX-XXXX / XX-XXXXX-XXXX',
}


def DV_maker(v):
    if v >= 2:
        return 11 - v
    return 0


def validate_cpf(value):

    if value in EMPTY_VALUES:
        return u''
    if not value.isdigit():
        value = re.sub("[-\.]", "", value)
    orig_value = value[:]
    try:
        int(value)
    except ValueError:
        raise ValidationError(error_messages['digits_only'])
    if len(value) != 11:
        raise ValidationError(error_messages['max_digits'])
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(range(10, 1, -1))])
    new_1dv = DV_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(range(11, 1, -1))])
    new_2dv = DV_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        raise ValidationError(error_messages['invalid'])

    return orig_value


def validate_phone(value):
    phone_cel = re.compile(r'^\d{2}-\d{5}-\d{4}$')
    phone_home = re.compile(r'^\d{2}-\d{4}-\d{4}$')

    if len(value) > 13:
        raise ValidationError(error_messages['len_phone'])

    if not phone_home.search(value) and not phone_cel.search(value):
        raise ValidationError(error_messages['invalid_phone'])

    return value