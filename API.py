import os, sys, json, requests, configparser

url = 'https://sellen.okta.com/api/v1/users/'
key = ''
config = configparser.ConfigParser()

if not os.path.isfile('config.txt'):
    configFile = open('config.txt', 'w+')
    configFile.write('[Default]\nkey = ')
    configFile.close()
    print('A new config.txt file has been created. Please enter your API key into this file')
    sys.exit()

config.read('config.txt')

if 'Default' in config and 'key' in config['Default']:
    key = config['Default']['key']
else:
    print('config.txt is not properly formatted')
    sys.exit()

if key == '':
    print('API key is missing from config.txt')
    sys.exit()

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'SSWS ' + key
    }

def PrettyPrint(rawJson):
    print(json.dumps(json.loads(rawJson), indent=4, sort_keys=True))

def CreateUser(firstName, lastName, email, phone, eid):
    data = {
    'profile': {
        'firstName': firstName,
        'lastName': lastName,
        'email': email,
        'mobilePhone': phone,
        'login': email,
        'employeeNumber': eid
        },
    'groupIds': ['00gcbyakoaxiUq5pl1t7']
    }
    data = json.dumps(data)

    PrettyPrint(requests.post(url, data = data, headers = headers).text)

def DeleteUser(user):
    status = requests.delete(url + user, headers=headers).status_code
    while status != 404:
        status = requests.delete(url + user, headers=headers).status_code
    print('User {} has been deleted'.format(user))

def GetGroups(user):
    PrettyPrint(requests.get(url + user + '/groups', headers=headers).text) 

# Run API tests with a test user and the API functions above
testUser = {
    'firstName': 'test',
    'lastName': 'michael',
    'email': 'apitest@email.com',
    'phone': '+1-206-555-1212',
    'eid': '99999'
}

CreateUser(testUser['firstName'], testUser['lastName'], testUser['email'], testUser['phone'], testUser['eid'])
GetGroups(testUser['email'])
print('Press enter to continue or Ctrl + C to quit')
input()
DeleteUser(testUser['email'])