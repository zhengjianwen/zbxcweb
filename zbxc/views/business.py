from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.views import View
from zbxc.models import Business

class BusinessView(View):

    def get(self, request):
        data = Business.objects.filter(status=1).order_by('weight')
        print(data)
        return render(request, 'business.html', locals())