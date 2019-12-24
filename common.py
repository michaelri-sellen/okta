import json, os, sys, configparser

class Common:
    def __init__(self):
        self.okta_key = ''
        self.snowflake_key = ''
        parser = configparser.ConfigParser()

        if not os.path.isfile('config.txt'):
            configFile = open('config.txt', 'w+')
            configFile.write('[Okta]\nkey = \n\n[Snowflake]\nkey = ')
            configFile.close()
            print('A new config.txt file has been created. Please enter your API key into this file')
            sys.exit()

        parser.read('config.txt')

        if 'Okta' in parser and 'key' in parser['Okta']:
            self.okta_key = parser['Okta']['key']
        else:
            print('config.txt is not properly formatted')
            sys.exit()

        if 'Snowflake' in parser and 'key' in parser['Snowflake']:
            self.snowflake_key = parser['Snowflake']['key']
        else:
            print('config.txt is not properly formatted')
            sys.exit()

        if self.okta_key == '':
            print('Okta API key is missing from config.txt')
            sys.exit()

        if self.snowflake_key == '':
            print('Snowflake API key is missing from config.txt')
            sys.exit()
    
    def PrettyPrint(self, rawJson):
        print(json.dumps(json.loads(rawJson), indent=4, sort_keys=True))