from django.http import request
from django.shortcuts import render

def home(request):
    context = {
        'head': 'parts/head.html',
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
    }
    return render(request, 'common/main.html', context)


def main(request):
    context = {
        'head': 'parts/head.html',
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
    }
    return render(request, 'common/main.html', context)


def error404(request):
    context = {
        'head': 'parts/head.html',
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
    }
    return render(request, 'common/404.html', context)


def about(request):
    context = {
        'head': 'parts/head.html',
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
    }
    return render(request, 'common/about.html', context)

def contact(request):
    context = {
        'head': 'parts/head.html',
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
    }
    return render(request, 'common/contact.html', context)


def propertyAgent(request):
    context = {
        'head': 'parts/head.html',
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
    }
    return render(request, 'common/property-agent.html', context)


def propertyList(request):
    context = {
        'head': 'parts/head.html',
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
    }
    return render(request, 'common/property-list.html', context)


def propertyType(request):
    context = {
        'head': 'parts/head.html',
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
    }
    return render(request, 'common/property-type.html', context)


def testImonial(request):
    context = {
        'head': 'parts/head.html',
        'navi': 'parts/navi.html',
        'foot': 'parts/foot.html',
        'footer': 'parts/footer.html',
    }
    return render(request, 'common/testimonial.html', context)
