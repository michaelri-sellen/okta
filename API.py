import os, sys, json, requests, configparser

url = 'https://sellen.okta.com/api/v1/users/'
auth = ''
config = configparser.ConfigParser()

if not os.path.isfile('config.txt'):
    configFile = open('config.txt', 'w+')
    configFile.write('[Default]\nkey = ')
    configFile.close()
    print('A new config.txt file has been created. Please enter your API key into this file')
    sys.exit()

config.read('config.txt')

if 'Default' in config and 'key' in config['Default']:
    auth = config['Default']['key']
else:
    print('config.txt is not properly formatted')
    sys.exit()

if auth == '':
    print('API key is missing from config.txt')
    sys.exit()

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