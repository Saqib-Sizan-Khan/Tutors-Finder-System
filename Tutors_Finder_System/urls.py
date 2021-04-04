"""Tutors_Finder_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views as hviews
from educator import views as eviews
from studentParent import views as spviews
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', hviews.homePage,name='home'),

    #login code
    #path('educator/login/',auth_views.LoginView.as_view(template_name='educator/login.html'),name="login"),
    #path('educator/logout/',auth_views.LogoutView.as_view(template_name='educator/logout.html'),name="logout"),

    #educators url
    path('educatorauth/', eviews.educatorAuthication,name='educatorauth'),
    path('educator/heducatorsignup/',eviews.hEducatorSignup,name='heducatorsignup'),
    path('educator/oeducatorsignup/',eviews.oEducatorSignup,name='oeducatorsignup'),
    path('educator/educatorlogin/',eviews.educatorLogin,name="login"),
    path('educator/educatorlogin/educatorinfo',eviews.educatorProfile,name="educatorinfo"),
    path('educator/educatorlogin/educatorupdateinfo',eviews.educatorUpdateInfo,name="educatorupdateinfo"),
    path('educator/logout/',eviews.educatorLogout,name='educatorlogout'),

    #subject choice url
    path('educator/heducatorsignup/subjectchoicehome/',eviews.subjectChoiceHome,name='subjectchoicehome'),
    path('educator/heducatorsignup/subjectchoiceoutside/',eviews.subjectChoiceOutside,name='subjectchoiceoutside'),

    #parents url
    path('studentparentauth/', spviews.parentAuthication,name='parentauth'),
    path('studentparent/parentsignup/',spviews.parentSignUp,name='parentsignup'),
    path('studentparent/parentlogin/',spviews.parentLogin,name='parentlogin'),
    path('studentparent/parentlogin/personalinfo',spviews.profileInfo,name='parentinfo'),
    path('studentparent/parentlogin/updateinfo',spviews.updateInfo,name='updateinfo'),
    path('studentparent/parentlogin/searcheducator/',spviews.searchEducator,name='searcheducator'),
    path('studentparent/parentlogin/educatordetails/',spviews.showEducatorDetails,name='showeducatordetails'),
    path('studentparent/parentlogin/confirmrequest',spviews.confirmRequest,name='confirmrequest'),
    path('studentparent/logout/',spviews.logout,name='parentlogout'),

    path('educatorlist/', eviews.educatorList,name='educator List'),
]
