#Common settings and functionality for use in other scripts can be found in this script
import json, os, sys, configparser #Required modules

class Common:
    class Okta_Config: #Define Okta settings before loading in the values from config.txt
        def __init__(self):
            self.key = ''
            self.users_url = ''
            self.apps_url = ''
            self.group_id = ''
            self.etoolbox_id = ''
            self.keystyle_id = ''
            self.headers = ''

    class Snowflake_Config: #Define Snowflake settings before loading in the values from config.txt
        def __init__(self):
            self.key = ''
            self.user = ''
            self.account = ''
            self.warehouse = ''
            self.database = ''
            self.schema = ''

    def __init__(self): #Constructor runs when a new instance of the Common class is created with Common()
        #Create new instances of Okta_Config and Snowflake_Config as attributes of Common.
        # This allows the settings to be accessed from other scripts using Common().okta_config.key, for example
        self.okta_config = self.Okta_Config()
        self.snowflake_config = self.Snowflake_Config()
        
        parser = configparser.ConfigParser() #Create a new instance of ConfigParser to load values from config.txt
        #List the names of the parameters to load from config.txt
        # By listing them here, we can ensure that a newly generated config.txt and an existing config.txt are properly formatted
        okta_params = ('key', 'url', 'group', 'etoolbox', 'keystyle')
        snowflake_params = ('key', 'user', 'account', 'warehouse', 'database', 'schema')

        #Check to see if config.txt exists, and generate a new config.txt if it doesn't
        if not os.path.isfile('config.txt'):
            configFile = open('config.txt', 'w+')
            
            configFile.write(
                '[Okta]\n{} = \n{} = \n{} = \n{} = \n {} = \n\n[Snowflake]\n{} = \n{} = \n{} = \n{} = \n{} = \n{} = '.format(
                    okta_params[0], okta_params[1], okta_params[2], okta_params[3], okta_params[4],
                    snowflake_params[0], snowflake_params[1], snowflake_params[2], snowflake_params[3], snowflake_params[4], snowflake_params[5]
                )
            )
            
            configFile.close()
            print('A new config.txt file has been created. Please enter your configuration details into this file')
            sys.exit()

        parser.read('config.txt') #Load config.txt

        #Check the loaded config.txt to ensure that it is formatted properly
        if all(s in parser for s in ('Okta', 'Snowflake')) and \
           all(s in parser['Okta'] for s in okta_params) and \
           all(s in parser['Snowflake'] for s in snowflake_params):
            
            #Loaded config.txt was formatted properly, now we read the values from it
            self.okta_config.key = parser['Okta'][okta_params[0]]
            self.okta_config.users_url = parser['Okta'][okta_params[1]] + '/users/'
            self.okta_config.apps_url = parser['Okta'][okta_params[1]] + '/apps/'
            self.okta_config.group_id = parser['Okta'][okta_params[2]]
            self.okta_config.etoolbox_id = parser['Okta'][okta_params[3]]
            self.okta_config.keystyle_id = parser['Okta'][okta_params[4]]

            self.snowflake_config.key = parser['Snowflake'][snowflake_params[0]]
            self.snowflake_config.user = parser['Snowflake'][snowflake_params[1]]
            self.snowflake_config.account = parser['Snowflake'][snowflake_params[2]]
            self.snowflake_config.warehouse = parser['Snowflake'][snowflake_params[3]]
            self.snowflake_config.database = parser['Snowflake'][snowflake_params[4]]
            self.snowflake_config.schema = parser['Snowflake'][snowflake_params[5]]
        else: #Something was missing from config.txt
            print('config.txt is not properly formatted')
            sys.exit()
        
        #Make sure none of the values in the Okta section of config.txt were empty
        okta_vars = vars(self.okta_config)
        for attribute in okta_vars.keys():
            if not attribute == 'headers' and not okta_vars[attribute]:
                print('{} is missing from the Okta section of config.txt'.format(attribute))
                sys.exit()

        #Make sure none of the values in the Snowflake section of config.txt were empty
        snoflake_vars = vars(self.snowflake_config)
        for attribute in snoflake_vars.keys():
            if not snoflake_vars[attribute]:
                print('{} is missing from the Snowflake section of config.txt'.format(attribute))
                sys.exit()

        #Add the header information using the key that was loaded from config.txt
        self.okta_config.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'SSWS ' + self.okta_config.key
        }
    
    def PrettyPrint(self, rawJson): #Display JSON in a human-readable format
        print(json.dumps(json.loads(rawJson), indent=4, sort_keys=True))