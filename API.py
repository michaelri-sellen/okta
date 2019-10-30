import json, requests, configparser

url = 'https://sellen.okta.com/api/v1/users/'
config = configparser.ConfigParser()
config.readfp(open('config.txt'))

auth = config.get('Default', 'key')
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'SSWS ' + auth
    }
data = {
    'profile': {
        'firstName': 'test',
        'lastName': 'michael',
        'email': 'apitest@sellen.com',
        'login': 'apitest@sellen.com',
    }
}

data = json.dumps(data)
r = requests.post(url, data = data, headers = headers).text
#r = requests.delete('https://sellen.okta.com/api/v1/users/apitest@sellen.com').text
j = json.dumps(json.loads(r), indent = 4, sort_keys = True)
print(j)