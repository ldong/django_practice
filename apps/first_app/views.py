from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    print 'something'
    return HttpResponse('hello');