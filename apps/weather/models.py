from django.db import models
import json, requests, logging

logger = logging.getLogger(__name__)

class WunderGround():
	'API to get weather information from WunderGround public webservices'

	def __init__(self, apikey):
		"""Constructor
		:parameter apikey: string(datatype)- gets WunderGround's API key
		"""
		self.__apikey = apikey
		self.url = "http://api.wunderground.com/api/" + self.__apikey
   	
   	def __request(self, url, headers, timeout):
   		response = requests.get(url, headers = headers, timeout = timeout)
		logger.info("url =" +url + "status_code=" + str(response.status_code))
		if response.status_code != requests.codes.ok: return None
		return response.json()

	def get_conditions_by_zipcode(self, zipcode):
		
		url = self.url + "/geolookup/conditions/q/" + str(zipcode) + ".json"
		print url;

		headers ={
		"Host"		: "api.wunderground.com",
		"X-Target-URI" : "http://api.wunderground.com",
		"Connection" : "Keep-Alive"
		}

		result = self.__request(url, headers, 5)
		return result

	def get_conditions_by_city(self, city, state):
		city = city.replace(" ", "_")
		url = self.url + "/conditions/q/" +state +"/" +city +".json"
		headers ={
			"Host"			: "api.wunderground.com",
			"X-Target-URI" 	: "http://api.wunderground.com",
			"Connection" 	: "Keep-Alive"
		}

		result = self.__request(url, headers, 5)
		return result

class Zipcode(models.Model):

	zipcode = models.PositiveSmallIntegerField(default = 0)
	zipimg = models.CharField(max_length =200)
	ziptemp = models.DecimalField(max_digits =5, decimal_places =2)

	def get_current_weather(self):
		keyfile = open("/tmp/wunderground.apikey", "r")
		key = keyfile.readline().rstrip()

		wg = WunderGround(key)
		data = wg.get_conditions_by_zipcode(self.zipcode)

		if data == None: return "Fail"
		if data != None:
			return {
			    "temp" : data["current_observation"]["temp_f"],
			    "city" : data["location"]["city"],
			    "state" : data["location"]["state"]
			}
