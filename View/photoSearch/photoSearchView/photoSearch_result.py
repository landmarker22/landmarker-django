from django.shortcuts import render


def photoSearch_result(request):
    imgname = request.POST["imgname"]
    print("이미지이름:\n",imgname)

    placeName = '경복궁'

    context = {
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
        'center': 'photoSearch/photoSearch_result.html',
        'placeName': placeName,
        'imgname': imgname
    }
    return render(request, 'photoSearch/photoSearch.html', context)