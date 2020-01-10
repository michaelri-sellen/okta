from common import Common
common = Common()

class Config:
    def __init__(self):
        self.users_url = 'https://sellen.okta.com/api/v1/users/'
        self.apps_url = 'https://sellen.okta.com/api/v1/apps/'
        self.group_id = '00gcbyakoaxiUq5pl1t7'
        self.etoolbox_id = '0oa8h5j3vgJAoMJrh1t7'
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'SSWS ' + common.okta_key
        }