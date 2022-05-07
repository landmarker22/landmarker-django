from django.http import request
from django.shortcuts import render
import Model.AI.test as ai
import Model.login.login_controller as lc

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
    print(ai.run('20210511_105221.jpg'))

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


def login(request):
    if request.method == 'GET':
        link_key = request.GET['link_key']

        lc.deleteDate()
        user_no = lc.selectLink(link_key)
        lc.deleteKey(link_key)
        request.session['user_no'] = user_no

        return render(request, 'login/login.html')
    else:
        return render(request, 'login/login.html')


def logout(request):
    if request.session['user_no'] != None:
        del request.session['user_no']

    return render(request, 'login/logout.html')
