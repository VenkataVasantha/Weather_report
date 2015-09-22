from django.shortcuts import render
from django.http import HttpResponse

from .models import Zipcode

def index(request):
	data = {
		'cities' : [
			{'zip': 95041, 'image': 'http://isvr.net/usr/1965629748/CustomPages/images/Cupertino.jpg', 'city': 'Cupertino' },
			{'zip': 94536, 'image': 'https://upload.wikimedia.org/wikipedia/commons/6/6f/Mission-Peak-2006.jpg', 'city': 'Fremont' },
			{'zip': 95035, 'image': 'https://c1.staticflickr.com/7/6228/6297777295_a4d1fe293a_b.jpg', 'city': 'Milpitas' },
			{'zip': 94035, 'image': 'http://travellingworm.files.wordpress.com/2013/08/mountainview_20130730_2.jpg', 'city': 'Mountain View' },
			{'zip': 94601, 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/OAKLAND%2C_CA%2C_USA_-_Skyline_and_Bridge.JPG/250px-OAKLAND%2C_CA%2C_USA_-_Skyline_and_Bridge.JPG', 'city': 'Oakland' },
			{'zip': 94101, 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/SF_From_Marin_Highlands3.jpg/800px-SF_From_Marin_Highlands3.jpg', 'city': 'San Francisco' },
			{'zip': 95054, 'image': 'https://upload.wikimedia.org/wikipedia/commons/a/a6/Santaclaraconventioncenter.jpg', 'city': 'Santa Clara' },
			{'zip': 94085, 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Murphystreetsunnyvale.jpg/250px-Murphystreetsunnyvale.jpg', 'city': 'Sunnyvale' },
			{'zip': 95101, 'image': 'https://upload.wikimedia.org/wikipedia/commons/2/27/San_Jose_California_Skyline.jpg', 'city': 'San Jose' },
		]	
	}
	return render(request, 'weather/index.html', data)

def results(request, zipcode):
	z = Zipcode.objects.get(zipcode=zipcode)
	temp = z.get_current_weather()
	data = {
		'zipcode' : zipcode,
		'temp'  : str(temp),
	}

	return render(request, 'weather/report.html', data)
