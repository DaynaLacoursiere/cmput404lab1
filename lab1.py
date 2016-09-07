import requests

response = requests.post('http://ccid-eddieantonio.rhcloud.com/dlacours')
print response.status_code