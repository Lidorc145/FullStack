from flask import Flask
import requests
app = Flask(__name__)

OpenWeatherMap_Key = '281d540454ca9e04172a926628313441'
Giphy_Key = '04Uu2Z5mZ56NB3g9vwCq4WkDpkgoGzIN'
city={'London', 'Tel Aviv', 'New York', 'Eilat','Berlin','Rio', 'Rome' ,'Moscow', 'Tiberias', 'San José', 'Bucharest','Nairobi'}


@app.route('/')
def city_search():
	cityInfo="";
	count=0
	for c in city:
		count+=1
		cityInfo+="<td>"+weather(c)+"</td>"
		if count%4 ==0:
			cityInfo+="<br></tr><tr>"
	html='<html><body><div align=center><h1>Please enter city to get weather information: <input type="text" name="city"><button type="submit" onClick="window.location.href = \'weather/\'+document.getElementsByName(\'city\')[0].value">Show Weather</button></h1><br><br><table><tr>'+cityInfo+'</tr></table>Lidor Cohen</div></body></html>'
	return html

@app.route('/weather/<city>')
def CityPage(city):
	return "<html><body><div align=center>"+weather(city)+"</div></body></html>"


def weather(city):
	OpenWeatherMap_Key = '281d540454ca9e04172a926628313441'
	url = 'http://api.openweathermap.org/data/2.5/weather'
	params = {'q': city, 'units': 'metric', 'appid': OpenWeatherMap_Key}
	response = requests.get(url = url, params = params)
	if int(response.json()['cod']) == 200:
		giphy_Word= str(WeaterGiphyWord(int(response.json()['main']['temp'])))
		giphy_url = 'http://api.giphy.com/v1/gifs/search'
		giphy_params = {'api_key':Giphy_Key, 'q': giphy_Word, 'limit': 1}
		giphy_response = requests.get(url = giphy_url, params = giphy_params)
		giphy_url = str(giphy_response.json()["data"][0]['images']['fixed_height']['url'])	 
		return '<b>Temperature in ' + city + ' is: ' + str(response.json()['main']['temp'])+'°</b><br><img src="'+giphy_url+'" height=200 width=250><br>'
	else: 
		return '<p style="color:red;"><b> Error with city name, please try again:</b></p><h1>Please enter city to get weather information: <input type="text" name="city"><button type="submit" onClick="window.location.href = \'\'+document.getElementsByName(\'city\')[0].value">Show Weather</button></h1>'

def WeaterGiphyWord(temp):
	if temp > 35:
		return "Weather piping hot day summer"
	if temp > 30:
		return "Weather summer day"
	if temp > 25:
		return "Weather nice day"
	if temp > 20:
		return "Weather cloudy day"
	if temp > 15:
		return "dog rainy day"
	if temp > 10:
		return "weather Ice cold day"
	return "frozen cold disney"
		

if __name__ == "__main__":
	app.run()
