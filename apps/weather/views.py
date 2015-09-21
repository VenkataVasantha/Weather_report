from django.shortcuts import render
from django.http import HttpResponse

from .models import Zipcode

def index(request):
	return HttpResponse("Hello")

def results(request, zipcode):
	z = Zipcode.objects.get(id=1)
	report = z.get_current_weather()

	return HttpResponse("Temp at Zip %s is %s" %(zipcode, report))