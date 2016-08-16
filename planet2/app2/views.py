from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import  get_object_or_404,render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse 
from django.core import serializers
from django.http import JsonResponse
import json
import os
import re 
from app2.models import Planet
from django.shortcuts import render_to_response
# from django.contrib.auth.models import Planets
def file_create(response):

	with open('planets.json') as f:
	  read = f.read()
	data = json.loads(read)
	for i in data:
		a=i['name']
		b=i['caption']
		c=i['temperature']
		e=i['radius']
		d=i['detail']
		g= i['image']
		savedata =Planet(name=a,caption=b,temperature=c,radius=e,detail=d, images = g)
		savedata.save()
	
 	x = serializers.serialize("json", Planet.objects.all())
 	
 	
	return JsonResponse( x,safe=False)

	
def single(request,i):
	x = Planet.objects.filter( id=int(i))
	# l=[]
	# l.append(x)
	# print l
	# nem = {'x' :x}
	return HttpResponse(x)
