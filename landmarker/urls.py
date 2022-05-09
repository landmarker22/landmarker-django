"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.landmarker, name='landmarker')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='landmarker')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from View.gallery import gallery
from View.home import home
from View.chatbot import chatbot
from View.photoSearch.photoSearchView import photoSearchView, photoSearch_result

urlpatterns = [
    path('landmarker/', home.home, name='home'),
    path('landmarker/main.do', home.main, name='main'),
    path('landmarker/error404.do', home.error404, name='error404'),
    path('landmarker/about.do', home.about, name='about'),
    path('landmarker/contact.do', home.contact, name='contact'),
    path('landmarker/propertyAgent.do', home.propertyAgent, name='propertyAgent'),
    path('landmarker/propertyList.do', home.propertyList, name='propertyList'),
    path('landmarker/propertyType.do', home.propertyType, name='propertyType'),
    path('landmarker/testImonial.do', home.testImonial, name='testImonial'),
    path('landmarker/chatbot.do', chatbot.chatbot, name='chatbot'),
    path('landmarker/chattrain', chatbot.chattrain, name='chattrain'),
    path('landmarker/chatanswer', chatbot.chatanswer, name='chatanswer'),


    # 로그인
    path('landmarker/login.do', home.login, name='login'),
    path('landmarker/logout.do', home.logout, name='logout'),

    # 이미지 검색
    path('landmarker/photoSearch.do${sessionScope.loginUser}', photoSearchView.photoSearch, name='photoSearch'),
    path('landmarker/photoSearch_result.do', photoSearch_result.photoSearch_result, name='photoSearch_result'),

    # 갤러리
    path('landmarker/gallery.do', gallery.gallery, name='gallery'),
    path('landmarker/gwrite.do', gallery.gwrite, name='gwrite'),
    path('landmarker/gupload.do', gallery.gupload, name='gupload'),
    path('landmarker/gallike.do', gallery.gallike, name='gallike'),
    path('landmarker/galsearch.do', gallery.galsearch, name='galsearch'),
    path('landmarker/gdetail.do', gallery.gdetail, name='gdetail'),
    path('landmarker/galreply.do', gallery.galreply, name='galreply'),
    path('landmarker/gdetailview.do', gallery.gdetailview, name='gdetailview'),
]
