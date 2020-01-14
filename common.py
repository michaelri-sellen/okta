import json, os, sys, configparser

class Common:
    class Okta_Config:
        def __init__(self):
            self.key = ''
            self.users_url = ''
            self.apps_url = ''
            self.group_id = ''
            self.app_id = ''
            self.headers = ''

    class Snowflake_Config:
        def __init__(self):
            self.key = ''
            self.user = ''
            self.account = ''
            self.warehouse = ''
            self.database = ''
            self.schema = ''

    def __init__(self):
        self.okta_config = self.Okta_Config()
        self.snowflake_config = self.Snowflake_Config()
        
        parser = configparser.ConfigParser()
        okta_params = ('key', 'url', 'group', 'app')
        snowflake_params = ('key', 'user', 'account', 'warehouse', 'database', 'schema')

        if not os.path.isfile('config.txt'):
            configFile = open('config.txt', 'w+')
            
            configFile.write(
                '[Okta]\n{} = \n{} = \n{} = \n{} = \n\n[Snowflake]\n{} = \n{} = \n{} = \n{} = \n{} = \n{} = '.format(
                    okta_params[0], okta_params[1], okta_params[2], okta_params[3],
                    snowflake_params[0], snowflake_params[1], snowflake_params[2], snowflake_params[3], snowflake_params[4], snowflake_params[5]
                )
            )
            
            configFile.close()
            print('A new config.txt file has been created. Please enter your configuration details into this file')
            sys.exit()

        parser.read('config.txt')

        if all(s in parser for s in ('Okta', 'Snowflake')) and \
           all(s in parser['Okta'] for s in okta_params) and \
           all(s in parser['Snowflake'] for s in snowflake_params):
            self.okta_config.key = parser['Okta'][okta_params[0]]
            self.okta_config.users_url = parser['Okta'][okta_params[1]] + '/users/'
            self.okta_config.apps_url = parser['Okta'][okta_params[1]] + '/apps/'
            self.okta_config.group_id = parser['Okta'][okta_params[2]]
            self.okta_config.app_id = parser['Okta'][okta_params[3]]

            self.snowflake_config.key = parser['Snowflake'][snowflake_params[0]]
            self.snowflake_config.user = parser['Snowflake'][snowflake_params[1]]
            self.snowflake_config.account = parser['Snowflake'][snowflake_params[2]]
            self.snowflake_config.warehouse = parser['Snowflake'][snowflake_params[3]]
            self.snowflake_config.database = parser['Snowflake'][snowflake_params[4]]
            self.snowflake_config.schema = parser['Snowflake'][snowflake_params[5]]
        else:
            print('config.txt is not properly formatted')
            sys.exit()
        
        okta_vars = vars(self.okta_config)
        for attribute in okta_vars.keys():
            if not attribute == 'headers' and not okta_vars[attribute]:
                print('{} is missing from the Okta section of config.txt'.format(attribute))
                sys.exit()

        snoflake_vars = vars(self.snowflake_config)
        for attribute in snoflake_vars.keys():
            if not snoflake_vars[attribute]:
                print('{} is missing from the Snowflake section of config.txt'.format(attribute))
                sys.exit()

        self.okta_config.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'SSWS ' + self.okta_config.key
        }
    
    def PrettyPrint(self, rawJson):
        print(json.dumps(json.loads(rawJson), indent=4, sort_keys=True))