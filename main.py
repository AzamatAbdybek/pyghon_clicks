import requests


url = 'https://api.vk.ru/method/utils.getServerTime'

token = 'e09b3c80e09b3c80e09b3c80fde384ad40ee09be09b3c80878bcf5581ec03732fb3a677'
params = {
    'v': '5.199',
}
headers = {'Authorization': "Bearer {}".format(token)}
response = requests.get(url, headers=headers, params=params)

print(response.text)