import os, sys, configparser, snowflake.connector
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

class Config:
    def __init__(self):
        api_key = ''
        p_key = ''
        raw_p_key = ''
        parser = configparser.ConfigParser()

        if not os.path.isfile('config.txt'):
            configFile = open('config.txt', 'w+')
            configFile.write('[Okta]\nkey = \n\n[Snowflake]\nkey = ')
            configFile.close()
            print('A new config.txt file has been created. Please enter your API key into this file')
            sys.exit()

        parser.read('config.txt')

        if 'Snowflake' in parser and 'key' in parser['Snowflake']:
            api_key = parser['Snowflake']['key']
        else:
            print('config.txt is not properly formatted')
            sys.exit()

        if api_key == '':
            print('API key is missing from config.txt')
            sys.exit()
        
        with open('rsa_key.p8') as encrypted_key:
            p_key = serialization.load_pem_private_key(
                encrypted_key.read().encode('ascii'),
                password = api_key.encode(),
                backend = default_backend()
            )
        
        raw_p_key = p_key.private_bytes(
            encoding = serialization.Encoding.DER,
            format = serialization.PrivateFormat.PKCS8,
            encryption_algorithm = serialization.NoEncryption()
        )

        self.connection = snowflake.connector.connect(
            user = '',
            account = '',
            private_key = raw_p_key,
            warehouse = '',
            database = '',
            schema = ''
        )
    
    def __del__(self):
        if not self.connection is None:
            self.connection.close()