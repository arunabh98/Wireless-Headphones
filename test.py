import requests

with open('music/test.mp3', mode='rb') as file:
    fileContent = file.read()
    for line in fileContent:
        r = requests.post('http://192.168.0.120/wireless_data', data = {'key':line})
