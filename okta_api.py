import json, requests
from okta_config import Config
from okta_common import Common

class API:
    def __init__(self):
        self.config = Config()
        self.common = Common()

    def CreateUser(self, firstName, lastName, email, phone, eid):
        data = {
        'profile': {
            'firstName': firstName,
            'lastName': lastName,
            'email': email,
            'mobilePhone': phone,
            'login': email,
            'employeeNumber': eid
            },
        'groupIds': [self.config.group_id]
        }
        data = json.dumps(data)

        self.common.PrettyPrint(requests.post(self.config.url, data = data, headers = self.config.headers).text)

    def DeleteUser(self, user):
        status = requests.delete(self.config.url + user, headers=self.config.headers).status_code
        while status != 404:
            status = requests.delete(self.config.url + user, headers=self.config.headers).status_code
        print('User {} has been deleted'.format(user))

    def GetGroups(self, user):
        self.common.PrettyPrint(requests.get(self.config.url + user + '/groups', headers=self.config.headers).text) 