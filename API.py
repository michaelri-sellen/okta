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


def CreateUser(firstName, lastName, email, eid):
    data = {
    'profile': {
        'firstName': firstName,
        'lastName': lastName,
        'email': email,
        'login': email,
        'employeeNumber': eid
        }
    }
    data = json.dumps(data)

    print(
        json.dumps(
            json.loads(requests.post(url, data = data, headers = headers).text), 
            indent = 4, sort_keys = True
        )
    )

def DeleteUser(user):
    r = requests.delete(url + user, headers=headers).status_code
    while r != 404:
        r = requests.delete(url + user, headers=headers).status_code
    print('User {} has been deleted'.format(user))


# Run API tests with a test user and the API functions above
testUser = {
    'firstName': 'test',
    'lastName': 'michael',
    'email': 'apitest@sellen.com',
    'eid': '99999'
}

CreateUser(testUser['firstName'], testUser['lastName'], testUser['email'], testUser['eid'])
print('Press enter to continue or Ctrl + C to quit')
input()
DeleteUser(testUser['email'])