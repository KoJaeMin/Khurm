import requests

headers={}
headers['Authorization']='Token '

r=requests.get('http://127.0.0.1:8000/folder/accounts/', headers=headers)