from django.http import request
from django.shortcuts import render

def gdetail(request):

    return render(request, 'common/gdetail.html')