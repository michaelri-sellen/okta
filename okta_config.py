import os, sys, configparser

class Config:
    def __init__(self):
        self.url = 'https://sellen.okta.com/api/v1/users/'
        self.group_id = '00gcbyakoaxiUq5pl1t7'

        key = ''
        parser = configparser.ConfigParser()

        if not os.path.isfile('config.txt'):
            configFile = open('config.txt', 'w+')
            configFile.write('[Okta]\nkey = ')
            configFile.close()
            print('A new config.txt file has been created. Please enter your API key into this file')
            sys.exit()

        parser.read('config.txt')

        if 'Okta' in parser and 'key' in parser['Okta']:
            key = parser['Okta']['key']
        else:
            print('config.txt is not properly formatted')
            sys.exit()

        if key == '':
            print('API key is missing from config.txt')
            sys.exit()


        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'SSWS ' + key
        }