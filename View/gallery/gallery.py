import json

from django.contrib.auth import authenticate, login
from django.http import request, JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import common.oracle_db as odb
import Model.gallery.gallery_class as gclass
import Model.gallery.gallery_controller as gcontroller
import Model.login.login_controller as lc


def gallery(request):
    data = gcontroller.select_all(7, 0)
    print(data)
    context = {
        'head': 'parts/head.html',
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
        'data': data,
        'user': lc.userLoad(request)
    }

    return render(request, 'common/gallery.html', context)


def gdetail(request):
    print('상세게시글번호 : ', request.GET['g_no'])
    data = gcontroller.select_one(request.GET['g_no'], 7)
    print('상세게시글 data : ', data)
    context = {
        'detail': data[0],
        'comment': data[1],
        'like_count': data[2][0],
        'like': data[3][0],
        'c_count': data[4][0],
        'user': lc.userLoad(request)
    }

    # return HttpResponse(json.dumps(data), content_type='application/json')
    return render(request, 'common/gdetail.html', context)


def gallike(request):
    gcontroller.gallike(request.GET['g_no'], request.GET['u_no'], request.GET['onoff'])
    data = gcontroller.select_one(request.GET['g_no'], 7)
    print('상세게시글 data : ', data)
    context = {
        'detail': data[0],
        'comment': data[1],
        'like_count': data[2][0],
        'like': data[3][0],
        'c_count': data[4][0],
        'user': lc.userLoad(request)
    }

    # return HttpResponse(json.dumps(data), content_type='application/json')
    return render(request, 'common/gdetail.html', context)


def galsearch(request):
    print('검색어 : ', request.GET['search'])
    data = gcontroller.search(request.GET['search'])
    print('상세게시글 data : ', data)
    context = {
        'data': data,
        'user': lc.userLoad(request)
    }

    # return HttpResponse(json.dumps(data), content_type='application/json')
    return render(request, 'common/gsearch.html', context)
