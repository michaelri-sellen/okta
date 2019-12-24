import snowflake.connector
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization
from common import Common

common = Common()

class DB:
    def __init__(self):
        p_key = ''
        raw_p_key = ''
        
        with open('rsa_key.p8') as encrypted_key:
            p_key = serialization.load_pem_private_key(
                encrypted_key.read().encode('ascii'),
                password = common.snowflake_key.encode(),
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