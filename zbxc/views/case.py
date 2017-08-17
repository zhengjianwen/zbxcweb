from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.views import View
from zbxc.models import CaseModel

class Case(View):

    def get(self, request):
        data = CaseModel.objects.filter(status=1).order_by('weight')
        return render(request, 'case.html', locals())