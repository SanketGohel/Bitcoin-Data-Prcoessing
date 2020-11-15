import requests
from assessment import price_result, create_file

def main():
	"""
	Main function will convert the data into json format and storing into Data varaible	

	"""
	url = 'https://api.coinranking.com/v1/public/coin/1/history/30d'
	get_data = requests.get(url)
	json_data = get_data.json()
	data = json_data['data']['history']
	
    #Calaculate the bitcoin price
	result = price_result(data)

    #Converting into JSON Format
	file = create_file(result)
	print(file)


if __name__ == "__main__":
	main()








