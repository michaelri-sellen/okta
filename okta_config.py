from okta_common import Common
common = Common()

class Config:
    def __init__(self):
        self.url = 'https://sellen.okta.com/api/v1/users/'
        self.group_id = '00gcbyakoaxiUq5pl1t7'
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'SSWS ' + common.okta_key
        }