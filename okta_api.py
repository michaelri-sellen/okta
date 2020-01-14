import json, requests
from common import Common

common = Common()
config = common.okta_config

class Okta:
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
            common.PrettyPrint(response.text)
            print("User {} has been added".format(email))
            self.__AddToEToolbox(json.loads(response.text)['id'], email)
        else:
            common.PrettyPrint(response.text)

    def __AddToEToolbox(self, userID, email):
        data = {
            'id': userID,
            'scope': 'USER',
            'credentials': {
                'userName': email,
                'password': {}
            }
        }
        data = json.dumps(data)

        response = requests.post(config.apps_url + config.app_id + '/users', data = data, headers = config.headers)

        if response.ok:
            print('E-Toolbox was assigned to the account {}'.format(email))
        else:
            common.PrettyPrint(response.text)

    def DeleteUser(self, user):
        status = requests.delete(config.users_url + user, headers=config.headers).status_code
        while status != 404:
            status = requests.delete(config.users_url + user, headers=config.headers).status_code
        print('User {} has been deleted'.format(user))
    
    def UpdateUser(self, eid, firstName, lastName, newEmail, phone):
        get_user = requests.get(config.users_url + '?search=profile.employeeNumber+eq+"{}"'.format(eid), headers = config.headers)
        
        if get_user.ok:
            user = json.loads(get_user.text)[0]['id']

            data = {
                'profile': {
                    'firstName': firstName,
                    'lastName': lastName,
                    'mobilePhone': phone,
                    'login': newEmail,
                    'email': newEmail,
                }
            }
            data = json.dumps(data)

            response = requests.post(config.users_url + user, data = data, headers = config.headers)

            if response.ok:
                print('The update to user {} was successful'.format(eid))
            else:
                common.PrettyPrint(response.text)
        else:
            common.PrettyPrint(get_user.text)