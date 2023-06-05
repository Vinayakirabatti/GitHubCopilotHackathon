# write a hello world code
import requests

city = input("Enter ity Name: ")
# api key - 9f538aec4ac2b2d79cdcfe4f69290c62
x = requests.get('https://api.openweathermap.org/data/2.5/weather?q=London&appid={9f538aec4ac2b2d79cdcfe4f69290c62}')

print(x.text)



# teting api - it takes 2 hours to activate the api key from weather
