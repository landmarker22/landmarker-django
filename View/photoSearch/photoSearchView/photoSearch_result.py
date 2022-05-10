import os
from PIL import Image
from django.shortcuts import render
from config.settings import BASE_DIR

def photoSearch_result(request):
    imgname = request.POST["imgname"]
    placeName = request.POST["landmark"]

    imgfilename = request.POST["imgfilename"]
    print("파일명:",imgfilename)

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
        'imgname': imgname
    }
    return render(request, 'photoSearch/photoSearch.html', context)

# def pname():
#     return placeName