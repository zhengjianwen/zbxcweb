from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.views import View
from zbxc.models import ZhaopinModel

class Zhaopin(View):

    def get(self, request):
        data = ZhaopinModel.objects.filter(status=1).order_by('weight')
        return render(request, 'zhaopin.html', locals())

class Jobs(View):

    def get(self, request,nid):
        data = ZhaopinModel.objects.filter(id=nid)
        return render(request, 'zhaopin.html', locals())