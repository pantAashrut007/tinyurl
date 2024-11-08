from django.shortcuts import render, HttpResponse
from .models import urlModel
import random
from django.shortcuts import redirect
from django.http import Http404

# Create your views here.

def home(request):
    #can return HTML files as well
    # return HttpResponse('Landing Page of tinyUrl')
    return render(request, 'landingPage.html')

def makeurlshort(request):
    if request.method == 'POST':
        longurl = request.POST['longurl']
        
        #create a shorturl
        def create_short_url():
            allowedChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            return ''.join(random.sample(allowedChars, 10))
        shorturl = create_short_url()
        obj = urlModel.objects.create(longurl = longurl, shorturl = shorturl)
        print("object created")
        shorturl = "http://localhost:8000/" + shorturl
    # return HttpResponse("Short URL for {} is : {}".format(longurl, shorturl))
    return render(request, 'urlCreated.html', context={'shorturl' : shorturl, 'longurl' : longurl})

def redirecturl(request, shorturl):
    print(shorturl)
    try:
        obj = urlModel.objects.get(shorturl = shorturl)
    except urlModel.DoesNotExist:
        obj = None
        
    if obj is not None:
        print("object found")
        print(obj.longurl)
        longurl = obj.longurl
        obj.count += 1
        obj.save()
        return redirect(obj.longurl)
    else:
        return HttpResponse("Check your URL")