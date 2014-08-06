from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.templatetags.static import static
import soundcloud

from django.template import Template, Context

#db imps
import psycopg2
from models import Toplist

def home(request):

        client = soundcloud.Client(client_id=[soundcloud_api_key])

	musicx=[]
	namex=[]
	
 	lst = Toplist.objects.all()
	count = len(lst)
	for l in lst:
        	play = client.get('/tracks/'+l.name)
        	
		s = client.get(play.stream_url, allow_redirects=False)	
	
		musicx.append(s.location)		
		namex.append(l)

	return render_to_response('index.html',{'musicx':musicx,'namex':namex,'count':count})
