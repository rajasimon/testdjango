# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == 'POST':
        print(request.POST.getlist('options'))
    return render(request, 'base.html')
