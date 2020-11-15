#import requests
import datetime
import time
import json


def price_result(data):
	result = []
	price = 0.0
	counter = 0

	for key in range(0,len(data)):
		"""
		Main logic of the funtion is to append new fields and calculating the difference of price of the last 30 days 

		Parameters
		Input(data[URL]): URL data which is nested dictionary 

		Return
		Output[result]: Nested Dictionary, filtering the data with time "00:00:00"
		"""
        
        #Converting timestamp to datetime in "yyyy-mm-dd HH:MM:SS"
		dt = datetime.datetime.fromtimestamp(data[key]['timestamp']//1000)
		time = str(dt)
		if '00:00:00' in time:

			#Calaculating day by week
			day = dt.strftime('%A')

            #calculating the difference between the privous dat price and current day price
			diff = float(data[key]['price']) - price
            
            #Storing the prive pervious day price
			price = float(data[key]['price'])

			#Scaling the direction of the price from pervious day
			scale = direction(diff)

			if not result:
				result.append({'price':data[key]['price'],'timestamp': time,'change':'NA','direction':'NA','day_of_week':day,'highSinceStart':0,'lowSinceStart':0})
			else:
				result.append({'price':data[key]['price'],'timestamp': time,'change':diff,'direction':scale,'day_of_week':day,'highSinceStart':0,'lowSinceStart':0})

            #calculating the min price of all the days
			mini = min(result,key = lambda item:item['price']) 
			#print('Min value:', mini['price'])
			if mini['price'] == data[key]['price']:
				lowSinceStart  = True
			else:
				lowSinceStart = False

			result[counter]['lowSinceStart'] = lowSinceStart
            
            #calculating the max price of all the days
			maxi = max(result,key = lambda item:item['price']) 
			#print('Min value:', mini['price'])
			if maxi['price'] == data[key]['price']:
				highSinceStart  = True
			else:
				highSinceStart = False

			#dis.append({'lowSinceStart': lowSinceStart})
			result[counter]['highSinceStart'] = highSinceStart
			counter+=1

	return result
			
		



def create_file(result):
	"""
    Laoding the nested Dictionary into JSON file format and saving with current date and time
    
    Parameters:
    Input:(result[list]): As a input passing nested dixtionary 
    
    Return
    Output(JSON Format):  Storing the data into JSON Format

	"""
	today = datetime.datetime.now()
	today = today.strftime("%Y-%m-%d_%H-%M-%S")
	#f =open(today, ".json", "w+")
	try:
		with open(today + '.json', 'w+') as json_file:
			json.dump(result, json_file)
		return "File, "+ today +".json has been created"
	except:
		return "Error occured while creating file"


def direction(diff):
	"""
    This function calculates the direction of the price from previous day price
    
    Parameters:
    Input(diff of price): Scaling the price in three type Up/Down/Same
    
    Return
    Output: Direction of the price from pervious day

	"""
	if diff > 0:
		direction = 'up'
	elif diff < 0:
		direction = 'down'
	else:
		direction = 'same'
	return direction






