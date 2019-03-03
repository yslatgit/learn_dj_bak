from django.test import TestCase
import requests,json

url = 'http://127.0.0.1:8000/learn/add_user/'
data = {'user':'松林','pwd':'12'}
req = requests.post(url,data)
print(req.text)
