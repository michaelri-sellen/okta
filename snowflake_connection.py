#This script will open a connection to the Snowflake database using key pair authentication
# It will also load additional configuration details from config.txt
# This script was made by following the example from the Snowflake documentation:
# https://docs.snowflake.net/manuals/user-guide/python-connector-example.html#using-key-pair-authentication
import snowflake.connector
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization
from common import Common

config = Common().snowflake_config

class Snowflake:
    #Constructor runs when a new instance of Snowflake is created with Snowflake()
    def __init__(self):
        p_key = '' #Place to store the encrypted private key
        raw_p_key = '' #Place to store the raw bytes of the private key
        
        #Load the encrypted private key into memory
        with open('rsa_key.p8') as encrypted_key:
            p_key = serialization.load_pem_private_key(
                encrypted_key.read().encode('ascii'),
                password = config.key.encode(),
                backend = default_backend()
            )
        
        #Get the raw bytes of the private key to secure the connection to Snowflake
        raw_p_key = p_key.private_bytes(
            encoding = serialization.Encoding.DER,
            format = serialization.PrivateFormat.PKCS8,
            encryption_algorithm = serialization.NoEncryption() #Snowflake won't be able to use the key if we encrypt it again
        )

        #Open the connection to Snowflake using the key and settings from config.txt
        # The connection is stored in the connection attribute so that it can be accessed using Snowflake().connection, for example
        self.connection = snowflake.connector.connect(
            user = config.user,
            account = config.account,
            private_key = raw_p_key,
            warehouse = config.warehouse,
            database = config.database,
            schema = config.schema
        )
    
    #Destructor runs when the Snowflake instance is no longer in scope
    # Ensures that the connection is properly and safely closed when not in use
    def __del__(self):
        if not self.connection is None:
            self.connection.close()