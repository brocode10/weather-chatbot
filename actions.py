from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import magicdate
import datetime
import dateutil.parser
import math
import string
import csv
from datetime import timedelta
import requests
import json
#TAB IS USED
from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionWeather(Action):
	def name(self):
		return 'action_weather'

	def run(self, dispatcher, tracker, domain):
		from apixu.client import ApixuClient
		api_key = 'xxxx' #your apixu key
		client = ApixuClient(api_key)

		location = tracker.get_slot('location')
		forecast = client.getForecastWeather(q=location, days=7)
		date = tracker.get_slot('date')
		no_of_days=tracker.get_slot('no_of_days')
		response=''
		if no_of_days:
			words = no_of_days.split()
			if hasNumbers(words[0]):
				no_days=words[0]
			else :
				no_days=text2int(words[0])
		#no_days=int(no_of_days)
		
		
			for i in range(0,no_days):
				city = forecast['location']['name']
				condition = forecast['forecast']['forecastday'][0]['day']['condition']['text']
				temperature_c = forecast['forecast']['forecastday'][0]['day']['avgtemp_c']
				humidity = forecast['forecast']['forecastday'][0]['day']['avghumidity']
				response = """{} is predicted in {} . The temperature would be {} degrees with humidity {}% .""".format(condition, city, temperature_c, humidity)
				dispatcher.utter_message(response)

			return [SlotSet("forecast",None),SlotSet("no_of_days",None),SlotSet("location",None)]
        
		if date:
			date_new = str(magicdate.magicdate(date))
			item=next(tracker.get_latest_entity_values("time"), None)
			string_date=str(item)
			true_date=string_date[:10]
			for i in range(0,7):
				if (true_date==forecast['forecast']['forecastday'][i]['date']):
					#country = forecast['location']['country']
					city = forecast['location']['name']
					condition = forecast['forecast']['forecastday'][i]['day']['condition']['text']
					temperature_c = forecast['forecast']['forecastday'][i]['day']['avgtemp_c']
					humidity = forecast['forecast']['forecastday'][i]['day']['avghumidity']
					#wind_mph = forecast['forecast']['forecastday'][i]['avghumidity']
					response = """{} is predicted in {} . The temperature would be {} degrees with humidity {}% .""".format(condition, city, temperature_c, humidity)
					dispatcher.utter_message(response)
					return[SlotSet("date",None),SlotSet("weather",None),SlotSet("location",None)]
			"""if not response:
				response="Please ask the information for next 7 days"
				dispatcher.utter_message(response)"""
		else:
			#country = forecast['location']['country']
			city = forecast['location']['name']
			condition = forecast['forecast']['forecastday'][0]['day']['condition']['text']
			temperature_c = forecast['forecast']['forecastday'][0]['day']['avgtemp_c']
			humidity = forecast['forecast']['forecastday'][0]['day']['avghumidity']
			#wind_mph = forecast['current']['wind_mph']

		response = """It is currently {} in {} . The temperature is {} degrees, the humidity is {}% .""".format(condition, city, temperature_c, humidity)

		dispatcher.utter_message(response)
		if "rain" in condition:
			dispatcher.utter_message("Please carry an umbrella or rain coat while going outdoors")
		return [SlotSet("weather",None),SlotSet("location",None)]
#TAB IS USED
class ActionTemp(Action):
	def name(self):
		return 'action_temp'
	def run(self,dispatcher,tracker,domain):
		from apixu.client import ApixuClient
		api_key = 'xxxx'
		client = ApixuClient(api_key)
		location = tracker.get_slot('location')
		forecast = client.getForecastWeather(q=location, days=7)
		date = tracker.get_slot('date')
		response=''
        #know_the_date = tracker.get_slot('know_the_date')
        #date_set = tracker.get_slot('date_set')
		if date:
			date_new = str(magicdate.magicdate(date))
			item=next(tracker.get_latest_entity_values("time"), None)
			string_date=str(item)
			true_date=string_date[:10]
			for i in range(0,7):
				if (true_date==forecast['forecast']['forecastday'][i]['date']):
					city = forecast['location']['name']
					temp = forecast['forecast']['forecastday'][i]['day']['avgtemp_c']
					response="""The temperature in {} would be {} degrees centigrade.""".format(city, temp)
					dispatcher.utter_message(response)
					return[SlotSet("date",None),SlotSet("temperature",None),SlotSet("location",None)]
			"""if not response:
				response="Please ask the information for next 7 days"
				dispatcher.utter_message(response)"""
		else:
			city = forecast['location']['name']
			temp = forecast['forecast']['forecastday'][0]['day']['avgtemp_c']
			response="""Currently, the temperature in {} is {} degrees centigrade.""".format(city, temp)
			dispatcher.utter_message(response)
			return[SlotSet("temperature",None),SlotSet("location",None)]

class ActionMaxTemp(Action):
	def name(self):
		return 'action_max_temp'
	def run(self,dispatcher,tracker,domain):
		from apixu.client import ApixuClient
		api_key = 'xxxx'

		client = ApixuClient(api_key)

		location = tracker.get_slot('location')
		forecast = client.getForecastWeather(q=location, days=7)
		date = tracker.get_slot('date')
		response=''
        #know_the_date = tracker.get_slot('know_the_date')
        #date_set = tracker.get_slot('date_set')
		if date:
			date_new = str(magicdate.magicdate(date))
			item=next(tracker.get_latest_entity_values("time"), None)
			string_date=str(item)
			true_date=string_date[:10]
			for i in range(0,7):
				if (true_date==forecast['forecast']['forecastday'][i]['date']):
					city = forecast['location']['name']
					max_temp = forecast['forecast']['forecastday'][i]['day']['maxtemp_c']

					response="""The maximum temperature in {} would be {} degrees centigrade""".format(city, max_temp)

					dispatcher.utter_message(response)
					return[SlotSet("date",None),SlotSet("maximum_temperature",None),SlotSet("location",None)]
			"""if not response:
				response="Please ask the information for next 7 days"
				dispatcher.utter_message(response)"""


		else:


			city = forecast['location']['name']
			max_temp = forecast['forecast']['forecastday'][0]['day']['maxtemp_c']

			response="""Today, the maximum temperature in {} is {} degrees centigrade""".format(city, max_temp)

			dispatcher.utter_message(response)
			return[SlotSet("maximum_temperature",None),SlotSet("location",None)]


class ActionMinTemp(Action):
	def name(self):
		return 'action_min_temp'
	def run(self,dispatcher,tracker,domain):
		from apixu.client import ApixuClient
		api_key = 'xxxx'

		client = ApixuClient(api_key)

		location = tracker.get_slot('location')
		forecast = client.getForecastWeather(q=location, days=7)
		date = tracker.get_slot('date')
		response=''
        #know_the_date = tracker.get_slot('know_the_date')
        #date_set = tracker.get_slot('date_set')
		if date:
			date_new = str(magicdate.magicdate(date))
			item=next(tracker.get_latest_entity_values("time"), None)
			string_date=str(item)
			true_date=string_date[:10]
			for i in range(0,7):
				if (true_date==forecast['forecast']['forecastday'][i]['date']):
					city = forecast['location']['name']
					min_temp = forecast['forecast']['forecastday'][i]['day']['mintemp_c']

					response="""The minimum temperature in {} would be {} degrees centigrade""".format(city, min_temp)

					dispatcher.utter_message(response)
					return[SlotSet("date",None),SlotSet("minimum_temperature",None),SlotSet("location",None)]
			"""if not response:
				response="Please ask the information for next 7 days"
				dispatcher.utter_message(response)"""


		else:


			city = forecast['location']['name']
			min_temp = forecast['forecast']['forecastday'][0]['day']['mintemp_c']

			response="""Today, the minimum temperature in {} is {} degrees centigrade""".format(city, min_temp)

			dispatcher.utter_message(response)
			return [SlotSet("minimum_temperature",None),SlotSet("location",None)]


class ActionWeatherCondition(Action):
	def name(self):
		return 'action_weather_cond'
	def run(self,dispatcher,tracker,domain):
		from apixu.client import ApixuClient
		api_key = 'xxxx'

		client = ApixuClient(api_key)
		location = tracker.get_slot('location')
		forecast = client.getForecastWeather(q=location, days=7)
		date = tracker.get_slot('date')
		response=''
        #know_the_date = tracker.get_slot('know_the_date')
        #date_set = tracker.get_slot('date_set')
		if date:
			date_new = str(magicdate.magicdate(date))
			item=next(tracker.get_latest_entity_values("time"), None)
			string_date=str(item)
			true_date=string_date[:10]
			for i in range(0,7):
				if (true_date==forecast['forecast']['forecastday'][i]['date']):
					city = forecast['location']['name']
					cond = forecast['forecast']['forecastday'][i]['day']['condition']['text']

					response="""It would be {} in {}.""".format(cond, city)
					dispatcher.utter_message(response)
					if "rain" in cond:
						dispatcher.utter_message("Please carry an umbrella or rain coat while going outdoors")
						

					

					return[SlotSet("date",None),SlotSet("condition",None),SlotSet("location",None)]
			"""if not response:
				response="Please ask the information for next 7 days"
				dispatcher.utter_message(response)"""


		else:

			city = forecast['location']['name']
			cond = forecast['forecast']['forecastday'][0]['day']['condition']['text']

			response="""It is currently {} in {}.""".format(cond, city)

			dispatcher.utter_message(response)
			if "rain" in cond:
				dispatcher.utter_message("Please carry an umbrella or rain coat while going outdoors")

			return [SlotSet("condition",None),SlotSet("location",None)]


class ActionTempComp(Action):
	def name(self):
		return 'action_temp_comp'

	def run(self,dispatcher,tracker,domain):
		from apixu.client import ApixuClient
		api_key = 'xxxx'

		client = ApixuClient(api_key)
		response=''

		location1 = tracker.get_slot('location1')
		location2 = tracker.get_slot('location2')

		forecast1 = client.getForecastWeather(q=location1,days=7)
		forecast2 = client.getForecastWeather(q=location2,days=7)
		date = tracker.get_slot('date')
		
        #know_the_date = tracker.get_slot('know_the_date')
        #date_set = tracker.get_slot('date_set')
		if date:
			date_new = str(magicdate.magicdate(date))
			item=next(tracker.get_latest_entity_values("time"), None)
			string_date=str(item)
			true_date=string_date[:10]
			for i in range(0,7):
				if (true_date==forecast1['forecast']['forecastday'][i]['date']):
					city1 = forecast1['location']['name']
					city2 = forecast2['location']['name']

					temp1 = forecast1['forecast']['forecastday'][i]['day']['avgtemp_c']
					temp2 = forecast2['forecast']['forecastday'][i]['day']['avgtemp_c']

					if (temp1>temp2):
						response="""{} would be hotter than {}.The temperature in {} would be {} whereas in {} would be {}.""".format(city1,city2,city1,temp1,city2,temp2)

					if (temp2>temp1):
						response="""{} would be hotter than {}.The temperature in {} would be {} whereas in {} would be {}.""".format(city2,city1,city2,temp2,city1,temp1)

					dispatcher.utter_message(response)
					return[SlotSet("date",None),SlotSet("compare",None),SlotSet("location1",None),SlotSet("location2",None),SlotSet("location",None)]

			"""if not response:
				response="Please ask the information for next 7 days"
				dispatcher.utter_message(response)"""



		else:

			city1 = forecast1['location']['name']
			city2 = forecast2['location']['name']

			temp1 = forecast1['forecast']['forecastday'][0]['day']['avgtemp_c']
			temp2 = forecast2['forecast']['forecastday'][0]['day']['avgtemp_c']

			if (temp1>temp2):
				response="""{} is hotter than {}.The temperature in {} is {} whereas in {} is {}.""".format(city1,city2,city1,temp1,city2,temp2)

			if (temp2>temp1):
				response="""{} is hotter than {}.The temperature in {} is {} whereas in {} is {}.""".format(city2,city1,city2,temp2,city1,temp1)

			dispatcher.utter_message(response)
			return [SlotSet("compare",None),SlotSet("location1",None),SlotSet("location2",None),SlotSet("location",None)]







class ActionHumid(Action):
	def name(self):
		return 'action_humid'
	def run(self,dispatcher,tracker,domain):
		from apixu.client import ApixuClient
		api_key = 'xxxx'
		client = ApixuClient(api_key)
		location = tracker.get_slot('location')
		forecast = client.getForecastWeather(q=location, days=7)
		date = tracker.get_slot('date')
		response=''
        #know_the_date = tracker.get_slot('know_the_date')
        #date_set = tracker.get_slot('date_set')
		if date:
			date_new = str(magicdate.magicdate(date))
			item=next(tracker.get_latest_entity_values("time"), None)
			string_date=str(item)
			true_date=string_date[:10]
			for i in range(0,7):
				if (true_date==forecast['forecast']['forecastday'][i]['date']):
					city = forecast['location']['name']
					humid = forecast['forecast']['forecastday'][i]['day']['avghumidity']
					response="""The humidity in {} would be {} percent.""".format(city, humid)
					dispatcher.utter_message(response)
					return[SlotSet("date",None),SlotSet("humidity",None),SlotSet("location",None)]
			"""if not response:
				response="Please ask the information for next 7 days"
				dispatcher.utter_message(response)"""
		else:
			city = forecast['location']['name']
			humid = forecast['forecast']['forecastday'][0]['day']['avghumidity']
			response="""Currently, the humidity in {} is {} percent.""".format(city, humid)
			dispatcher.utter_message(response)
			return[SlotSet("humidity",None),SlotSet("location",None)]


def text2int(textnum, numwords={}):
	if not numwords:
		units = [
			"zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
			"nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
			"sixteen", "seventeen", "eighteen", "nineteen",
			]

		tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

		scales = ["hundred", "thousand", "million", "billion", "trillion"]

		numwords["and"] = (1, 0)
		for idx, word in enumerate(units):  numwords[word] = (1, idx)
		for idx, word in enumerate(tens):       numwords[word] = (1, idx * 10)
		for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

	ordinal_words = {'a':1, 'first':1, 'second':2, 'third':3, 'fifth':5, 'eighth':8, 'ninth':9, 'twelfth':12}
	ordinal_endings = [('ieth', 'y'), ('th', '')]

	textnum = textnum.replace('-', ' ')

	current = result = 0
	for word in textnum.split():
		if word in ordinal_words:
			scale, increment = (1, ordinal_words[word])
		else:
			for ending, replacement in ordinal_endings:
				if word.endswith(ending):
					word = "%s%s" % (word[:-len(ending)], replacement)

			if word not in numwords:
				raise Exception("Illegal word: " + word)

			scale, increment = numwords[word]

		current = current * scale + increment
		if scale > 100:
			result += current
			current = 0

	return result + current

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)
