#coding:utf-8

from datetime import datetime


def convert_string_to_date(dt_str, format):
    return datetime.strptime(dt_str, format)