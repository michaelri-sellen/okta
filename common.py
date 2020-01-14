import json, os, sys, configparser

class Common:
    def __init__(self):
        self.okta_key = ''
        self.snowflake_key = ''
        self.snowflake_user = ''
        self.snowflake_account = ''
        self.snowflake_warehouse = ''
        self.snowflake_database = ''
        self.snowflake_schema = ''
        parser = configparser.ConfigParser()

        if not os.path.isfile('config.txt'):
            configFile = open('config.txt', 'w+')
            configFile.write('[Okta]\nkey = \n\n[Snowflake]\nkey = \nuser = \naccount = \nwarehouse = \ndatabase = \nschema = ')
            configFile.close()
            print('A new config.txt file has been created. Please enter your API key into this file')
            sys.exit()

        parser.read('config.txt')

        if 'Okta' in parser and 'key' in parser['Okta']:
            self.okta_key = parser['Okta']['key']
        else:
            print('config.txt is not properly formatted')
            sys.exit()

        if 'Snowflake' in parser and all(s in parser['Snowflake'] for s in ('key', 'user', 'account', 'warehouse', 'database', 'schema')):
            self.snowflake_key = parser['Snowflake']['key']
            self.snowflake_user = parser['Snowflake']['user']
            self.snowflake_account = parser['Snowflake']['account']
            self.snowflake_warehouse = parser['Snowflake']['warehouse']
            self.snowflake_database = parser['Snowflake']['database']
            self.snowflake_schema = parser['Snowflake']['schema']
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