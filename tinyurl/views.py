'''
responsible for the views to the user
'''
from django.shortcuts import HttpResponse
def sample(request):
    return HttpResponse("<H1> Hello </H1>")