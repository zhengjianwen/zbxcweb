"""webserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from .views.index import Index
from .views.about import About
from .views.business import BusinessView
from .views.case import Case
from .views.news import News
from .views.contact import Contact
from .views.zhaopin import Zhaopin, Jobs


urlpatterns = [
    url(r'^index.html$', Index.as_view()),
    url(r'^about.html$', About.as_view()),
    url(r'^business.html$', BusinessView.as_view()),
    url(r'^case.html$', Case.as_view()),
    url(r'^news.html$', News.as_view()),
    url(r'^contact.html$', Contact.as_view()),
    url(r'^zhaopin.html$', Zhaopin.as_view()),
    url(r'^zhaopin/jobs/(\d+).html$', Jobs.as_view()),
    url(r'^$', Index.as_view()),
]
