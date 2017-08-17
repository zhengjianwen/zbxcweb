from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.views import View
from zbxc.models import Filiale

class Contact(View):

    def get(self, request):
        data = Filiale.objects.filter(status=1).order_by('weight')
        return render(request, 'contact.html', locals())

    def post(self,request):

        pass