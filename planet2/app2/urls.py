from django.conf.urls import url
from.import views


urlpatterns=[

	
	url(r'^file/$', views.file_create, name="file_create"),
   # url(r'^description/$', views.description, name="description"),
   url(r'^(?P<i>[0-9]{1})/$', views.single, name="single"),
   
]	