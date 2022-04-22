from django.shortcuts import render


def photoSearch(request):
    context = {
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
    }
    return render(request, 'photoSearch/photoSearch.html', context)