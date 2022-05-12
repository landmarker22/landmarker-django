import random

from django.shortcuts import render
import json
import os

from Model.AI.test import run
from config.settings import BASE_DIR
from django.http import HttpResponse
import Model.login.login_controller as lc

def photoSearch(request):
    user = lc.userLoad(request)
    context = {
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
        'user': user
    }
    return render(request, 'photoSearch/photoSearch.html', context)

def photoSearch_ai(request):
    num = random.randrange(1000000000, 9999999999)
    img = request.FILES.get("uploadFiles")
    print(type(img))

    imgname = str(num)+"_"+img._name
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