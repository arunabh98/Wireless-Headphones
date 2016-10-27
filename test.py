import requests

with open('music/test1.wav', mode='rb') as file:
    fileContent = file.read()
    for line in fileContent:
        r = requests.post('http://192.168.0.112/login', data = {'CHARACTER':line})
