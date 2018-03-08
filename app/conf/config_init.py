#!/usr/bin/env python
#coding: utf-8

import os, sys, csv, django, argparse
from django.db.utils import IntegrityError
from settings import BASE_DIR

settings = {'local':'settings', 'production':'settings_production'}
parser = argparse.ArgumentParser(description='Populate words csv file in database')
parser.add_argument('-c', '--conf', dest='settings', help='name settings file ex: settings')
args = parser.parse_args()

sys.path.append(os.path.dirname(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings[args.settings] if args.settings else 'settings')
django.setup()

from main.models import StatusModel
from django.contrib.auth.models import User



def created_status_default():
    criada = StatusModel(name='criada')
    criada.save()
    delegada = StatusModel(name='delegada')
    delegada.save()
    finalizada = StatusModel(name='finalizada')
    finalizada.save()
    todos = StatusModel(name='todos')
    todos.save()

def created_superuser():
    username = 'root2'
    password = '123@@123'
    email = 'root@root.com'

    user = User(username=username, email=email)
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.is_active = True
    user.save()



if __name__ == '__main__':
    created_status_default()
    created_superuser()
