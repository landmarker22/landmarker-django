from django.shortcuts import render
import json
import os

from Model.AI.test import run
from config.settings import BASE_DIR
from django.http import HttpResponse

def photoSearch(request):
    context = {
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
    }
    return render(request, 'photoSearch/photoSearch.html', context)

def photoSearch_ai(request):

    img = request.FILES.get("uploadFiles")
    print(type(img))

    imgname = img._name
    f = open('%s/%s' % (os.path.join(BASE_DIR,"static/AI_img"), imgname), 'wb')
    for chunk in img.chunks():
        f.write(chunk)
        f.close()

    imgpath = os.path.join(BASE_DIR,"static/AI_img",imgname)
    # AI inference start
    inference = run(imgpath)
    print(inference)

    print("확인:",inference)

    data = [inference, imgname]

    print(data)

    return HttpResponse(json.dumps(data), content_type='application/json')