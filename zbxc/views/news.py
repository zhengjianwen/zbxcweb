from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.views import View


class News(View):

    def get(self, request):


        return render(request, 'news.html', locals())