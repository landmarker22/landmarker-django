import json
import os
from uuid import uuid4

from django.conf.global_settings import MEDIA_ROOT
from django.contrib.auth import authenticate, login
from django.http import request, JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import common.oracle_db as odb
import Model.gallery.gallery_class as gclass
import Model.gallery.gallery_controller as gcontroller
import Model.login.login_controller as lc


def gallery(request):
    user = lc.userLoad(request)

    if user != 0:
        data = gcontroller.select_all(user.get('user_no'), 0)
    else:
        data = gcontroller.select_all(user, 0)

    context = {
        'head': 'parts/head.html',
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
        'data': data,
        'user': user
    }

    return render(request, 'gallery/gallery.html', context)

def gdetailview(request):
    user = lc.userLoad(request)

    if (user != 0):
        data = gcontroller.select_one(request.GET['g_no'], user.get('user_no'))
    else:
        data = gcontroller.select_one(request.GET['g_no'], user)

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
        'user': user
    }

    return render(request, 'gallery/gdetailview.html', context)

def gwrite(request):
    print('글쓸유저번호 : ', request.POST['u_no'])
    context = {
        'user': lc.userLoad(request)
    }
    return render(request, 'gallery/gwrite.html', context)

def gupload(request):
    file = request.FILES['file']
    uuid_name = uuid4().hex+'.'+(file._name).split('.')[1]
    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', uuid_name)
    save_path = os.path.join("./static/gallery_images", uuid_name)
    with open(save_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    image = uuid_name
    content = request.POST['content']
    hashtag = request.POST['hashtag']

    # profile_image = request.data.get('profile_image')
    user_name = request.POST['user_name']

    user = lc.userLoad(request)

    if user != 0:
        gal = {'content': content, 'hashtag': hashtag, 'image': image, 'user_name': user_name, 'user_no': user.get('user_no')}
        gcontroller.insert_gallery(gal)
    else:
        print('유저세션 없음')

    return 0

def gmodify(request):
    content = request.POST['content']
    hashtag = request.POST['hashtag']
    g_no = request.POST['g_no']
    user = lc.userLoad(request)

    if user != 0:
        gal_modi = {'content': content, 'hashtag': hashtag, 'g_no': g_no}
        gcontroller.modify_gallery(gal_modi)
    else:
        print('유저세션 없음')

    return 0

def gdelete(request):
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', request)
    g_no = request.POST['g_no']
    user = lc.userLoad(request)
    if user != 0:
        gcontroller.delete_gallery(g_no)
    else:
        print('유저세션 없음')

    return 0

def gdetail(request):
    user = lc.userLoad(request)
    if user != 0:
        data = gcontroller.select_one(request.GET['g_no'], user.get('user_no'))
    else:
        data = gcontroller.select_one(request.GET['g_no'], user)
    print(data)
    context = {
        'detail': data[0],
        'comment': data[1],
        'like_count': data[2][0],
        'like': data[3][0],
        'c_count': data[4][0],
        'user': user
    }

    # return HttpResponse(json.dumps(data), content_type='application/json')
    return render(request, 'gallery/gdetail.html', context)

def galreply(request):
    user = lc.userLoad(request)
    gcontroller.insert_reply(request.POST['g_no'], request.POST['u_no'], request.POST['reply'])
    if(user != 0):
        data = gcontroller.select_one(request.POST['g_no'], user.get('user_no'))
    else:
        data = gcontroller.select_one(request.POST['g_no'], user)

    context = {
        'detail': data[0],
        'comment': data[1],
        'like_count': data[2][0],
        'like': data[3][0],
        'c_count': data[4][0],
        'user': user
    }

    return render(request, 'gallery/gdetail.html', context)

def delreply(request):
    user = lc.userLoad(request)
    gcontroller.delete_reply(request.POST['c_no'])
    if(user != 0):
        data = gcontroller.select_one(request.POST['g_no'], user.get('user_no'))
    else:
        data = gcontroller.select_one(request.POST['g_no'], user)

    context = {
        'detail': data[0],
        'comment': data[1],
        'like_count': data[2][0],
        'like': data[3][0],
        'c_count': data[4][0],
        'user': user
    }

    return render(request, 'gallery/gdetail.html', context)

def gallike(request):
    user = lc.userLoad(request)
    if(user != 0):
        gcontroller.gallike(request.GET['g_no'], user.get('user_no'), request.GET['onoff'])
        data = gcontroller.select_one(request.GET['g_no'], user.get('user_no'))
    else:
        gcontroller.gallike(request.GET['g_no'], user, request.GET['onoff'])
        data = gcontroller.select_one(request.GET['g_no'], user)

    context = {
        'detail': data[0],
        'comment': data[1],
        'like_count': data[2][0],
        'like': data[3][0],
        'c_count': data[4][0],
        'user': user
    }

    # return HttpResponse(json.dumps(data), content_type='application/json')
    return render(request, 'gallery/gdetail.html', context)


def galsearch(request):
    data = gcontroller.search(request.GET['search'])

    context = {
        'data': data,
        'user': lc.userLoad(request)
    }

    # return HttpResponse(json.dumps(data), content_type='application/json')
    return render(request, 'gallery/gsearch.html', context)

def galselect(request):
    user = lc.userLoad(request)
    if len(request.GET) == 0:
        op = 0
    else:
        op = request.GET['op']

    if user != 0:
        data = gcontroller.select_all(user.get('user_no'), op)
    else:
        data = gcontroller.select_all(user, op)
    context = {
        'data': data,
        'user': user
    }

    return render(request, 'gallery/gselect.html', context)
