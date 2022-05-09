import json

from django.contrib.auth import authenticate, login
from django.http import request, JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import Model.gallery.gallery_class as gclass
import Model.gallery.gallery_controller as gcontroller
import Model.login.login_controller as lc


def gallery(request):
    if(lc.userLoad(request) != 0):
        data = gcontroller.select_all(lc.userLoad(request).get('user_no'), 0)
    elif(lc.userLoad(request) == 0):
        data = gcontroller.select_all(lc.userLoad(request), 0)

    print(data)
    context = {
        'head': 'parts/head.html',
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
        'data': data,
        'user': lc.userLoad(request)
    }

    return render(request, 'gallery/gallery.html', context)


def gdetailview(request):
    print('request', request)
    print('상세게시글번호 : ', request.GET['g_no'])
    if(lc.userLoad(request) != 0):
        data = gcontroller.select_one(request.GET['g_no'], lc.userLoad(request).get('user_no'))
    elif(lc.userLoad(request) == 0):
        data = gcontroller.select_one(request.GET['g_no'], lc.userLoad(request))
    print('상세게시글 data : ', data)
    context = {
        'detail': data[0],
        'comment': data[1],
        'like_count': data[2][0],
        'like': data[3][0],
        'c_count': data[4][0],
        'head': 'parts/head.html',
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
        'data': data,
        'user': lc.userLoad(request)
    }

    return render(request, 'gallery/gdetailview.html', context)

def gwrite(request):
    print('글쓸유저번호 : ', request.POST['u_no'])
    context = {
        'user': lc.userLoad(request)
    }
    return render(request, 'gallery/gwrite.html', context)

def gupload(request):
    context = {
        'user': lc.userLoad(request)
    }
    return render(request, 'gallery/gwrite.html', context)


def gdetail(request):
    print('request', request)
    print('상세게시글번호 : ', request.GET['g_no'])
    if(lc.userLoad(request) != 0):
        data = gcontroller.select_one(request.GET['g_no'], lc.userLoad(request).get('user_no'))
    elif(lc.userLoad(request) == 0):
        data = gcontroller.select_one(request.GET['g_no'], lc.userLoad(request))
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
    return render(request, 'gallery/gdetail.html', context)

def galreply(request):
    print('댓글쓸게시글번호 : ', request.POST['g_no'], '댓글쓸유저넘버 : ', request.POST['u_no'])
    gcontroller.insert_reply(request.POST['g_no'], request.POST['u_no'], request.POST['reply'])
    if(lc.userLoad(request) != 0):
        data = gcontroller.select_one(request.POST['g_no'], lc.userLoad(request).get('user_no'))
    elif(lc.userLoad(request) == 0):
        data = gcontroller.select_one(request.POST['g_no'], lc.userLoad(request))
    print('상세게시글 data : ', data)
    context = {
        'detail': data[0],
        'comment': data[1],
        'like_count': data[2][0],
        'like': data[3][0],
        'c_count': data[4][0],
        'user': lc.userLoad(request)
    }

    return render(request, 'gallery/gdetail.html', context)

def gallike(request):
    if(lc.userLoad(request) != 0):
        gcontroller.gallike(request.GET['g_no'], lc.userLoad(request).get('user_no'), request.GET['onoff'])
        data = gcontroller.select_one(request.GET['g_no'], lc.userLoad(request).get('user_no'))
    elif(lc.userLoad(request) == 0):
        gcontroller.gallike(request.GET['g_no'], lc.userLoad(request), request.GET['onoff'])
        data = gcontroller.select_one(request.GET['g_no'], lc.userLoad(request))
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
    return render(request, 'gallery/gdetail.html', context)


def galsearch(request):
    print('검색어 : ', request.GET['search'])
    data = gcontroller.search(request.GET['search'])
    print('상세게시글 data : ', data)
    context = {
        'data': data,
        'user': lc.userLoad(request)
    }

    # return HttpResponse(json.dumps(data), content_type='application/json')
    return render(request, 'gallery/gsearch.html', context)
