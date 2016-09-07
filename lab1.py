import requests

response = requests.get('https://raw.githubusercontent.com/DaynaLacoursiere/cmput404lab1/master/lab1.py')
print response.text