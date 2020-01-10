import json, requests
from okta_config import Config
from common import Common

config = Config()
common = Common()

class API:
    def CreateUser(self, firstName, lastName, email, phone, eid, password = None):
        data = {
        'profile': {
            'firstName': firstName,
            'lastName': lastName,
            'email': email,
            'mobilePhone': phone,
            'login': email,
            'employeeNumber': eid
            },
        'groupIds': [config.group_id]
        }
        if password is not None:
            data['credentials'] = {
                'password': {
                    'value': password
                }
            }
        data = json.dumps(data)

        response = requests.post(config.users_url, data = data, headers = config.headers)
        
        if response.ok:
            print("User {} has been added".format(email))
            self.AddToEToolbox(json.loads(response.text)['id'], email)
        else:
            common.PrettyPrint(response.text)

    def AddToEToolbox(self, userID, email):
        data = {
            'id': userID,
            'scope': 'USER',
            'credentials': {
                'userName': email,
                'password': {}
            }
        }
        data = json.dumps(data)

        response = requests.post(config.apps_url + config.etoolbox_id + '/users', data = data, headers = config.headers)

        if response.ok:
            print('E-Toolbox was assigned to the account {}'.format(email))
        else:
            common.PrettyPrint(response.text)

    def DeleteUser(self, user):
        status = requests.delete(config.users_url + user, headers=config.headers).status_code
        while status != 404:
            status = requests.delete(config.users_url + user, headers=config.headers).status_code
        print('User {} has been deleted'.format(user))

    def GetGroups(self, user):
        common.PrettyPrint(requests.get(config.users_url + user + '/groups', headers=config.headers).text) 

    def __UpdateBase(self, user, data):
        data = json.dumps(data)
        response = requests.post(config.users_url + user, data = data, headers = config.headers)

        if response.ok:
            print('The update to user {} was successful'.format(user))
        else:
            common.PrettyPrint(response.text)

    def UpdateName(self, user, firstName, lastName):
        data = {
            'profile': {
                'firstName': firstName,
                'lastName': lastName,
            }
        }
        self.__UpdateBase(user, data)
    
    def UpdatePhone(self, user, phone):
        data = {
            'profile': {
                'mobilePhone': phone
            }
        }
        self.__UpdateBase(user, data)

    def UpdateEmail(self, user, newEmail):
        data = {
            'profile': {
                'login': newEmail,
                'email': newEmail,
            }
        }
        self.__UpdateBase(user, data)
    
    def UpdateAll(self, user, firstName, lastName, newEmail, phone):
        data = {
            'profile': {
                'firstName': firstName,
                'lastName': lastName,
                'mobilePhone': phone,
                'login': newEmail,
                'email': newEmail,
            }
        }
        self.__UpdateBase(user, data)

    def UpdateJobTitle(self, user, newTitle):
        data = {
            'profile': {
                'title': newTitle
            }
        }
        data = json.dumps(data)

        response = requests.post(config.users_url + user, data = data, headers = config.headers)

        if response.ok:
            print('User {} was successfully updated to the {} job title'.format(user, newTitle))
        else:
            common.PrettyPrint(response.text)