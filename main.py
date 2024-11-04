import requests

api_url = 'https://api.vk.com/method/utils.getShortLink'

long_url = 'https://kubernetes.io/docs/reference/kubectl/quick-reference/#updating-resources'

token = 'e09b3c80e09b3c80e09b3c80fde384ad40ee09be09b3c80878bcf5581ec03732fb3a677'


params = {
    'v': '5.199',
    'url': long_url,
    'access_token': token,
    'private': 0
}

response = requests.post(api_url, params=params)

print(response.json())
