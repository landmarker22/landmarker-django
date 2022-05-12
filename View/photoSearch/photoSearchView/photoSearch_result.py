import os
from PIL import Image
from django.shortcuts import render
from config.settings import BASE_DIR
import Model.login.login_controller as lc
import Model.gallery.gallery_controller as gcontroller
from datetime import datetime

# def time():
# #     now = datetime.now()
# #     ampm = now.strftime('%p')
# #     ampm_kr = '오전' if ampm == 'AM' else '오후'
# #
# #     if(now.minute < 9):
# #         min = str("0") + str(now.minute)
# #     else:
# #         min = str(now.minute)
# #     hour = now.hour - 12
# #     time = ampm_kr + " " + str(hour) + ":" + min
# #
# #     return time


def photoSearch_result(request):
    user = lc.userLoad(request)
    if user != 0:
        userName = user['user_name']
    else:
        userName = "비회원"

    now = datetime.now()
    ampm = now.strftime('%p')
    ampm_kr = '오전' if ampm == 'AM' else '오후'

    if (now.minute < 9):
        min = str("0") + str(now.minute)
    else:
        min = str(now.minute)
    hour = now.hour - 12
    time = ampm_kr + " " + str(hour) + ":" + min

    print()

    imgname = request.POST["imgname"]
    placeName = request.POST["landmark"]
    imgfilename = request.POST["imgfilename"]

    global place
    place = placeName

    if placeName == "잘못된 결과 신고하기":
        imgpath = os.path.join(BASE_DIR, "static/AI_img", imgfilename)
        print(imgpath)
        reportimg = Image.open(imgpath)
        reportimg.save(os.path.join(BASE_DIR, "static/report_img", imgfilename))

        context = {
            'navi': 'parts/navi.html',
            'foot': 'parts/foot.html',
            'footer': 'parts/footer.html',
        }
        return render(request, 'photoSearch/photoSearch.html', context)

    context = {
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
        'center': 'photoSearch/photoSearch_result.html',
        'placeName': placeName,
        'imgname': imgname,
        'userName': userName,
        'time': time,
        'user': user
    }
    return render(request, 'photoSearch/photoSearch.html', context)

def pname():
    return place