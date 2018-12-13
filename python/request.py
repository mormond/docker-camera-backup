import requests
import constants as c

url = c.notificationUrl
payload = { 'alerttype' : 'error', 'message' : '1' }

r = requests.post(url, json = payload)


