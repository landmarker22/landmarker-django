import json

from django.contrib.auth import authenticate, login
from django.http import request, JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import common.oracle_db as odb
import Model.gallery.gallery_class as gclass
import Model.gallery.gallery_controller as gcontroller


def gallery(request):
    data = gcontroller.select_all()
    context = {
        'head': 'parts/head.html',
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
        'data': data,
    }
    print(data[0])
    return render(request, 'common/gallery.html', context)


def gdetail(request):
    print('상세게시글번호 : ', request.GET['g_no'])
    data = gcontroller.select_one(request.GET['g_no'])
    print('상세게시글 data : ', data)
    context = {
        'data': data[0]
    }
    # return HttpResponse(json.dumps(data), content_type='application/json')
    return render(request, 'common/gdetail.html', context)
