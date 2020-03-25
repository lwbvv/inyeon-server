from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Candidate
# Create your views here.
# def index(request):
#     candidate = Candidate.objects.all()
#     str = ''
#     for candidate in candidate:
#         str +="<p>{} 기호{}번({})<br>".format(request.user,candidate.party_number, candidate.area)
#         str += candidate.introduction+"<p>"
#     return HttpResponse(str)
@csrf_exempt
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        instance = Candidate.objects.create(name = username,introduction = password, area = 'area', party_number = 1)
        return HttpResponse("instance")

    return HttpResponse("nono")
