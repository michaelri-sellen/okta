from okta_api import Okta
from snowflake_connection import Snowflake

okta = Okta()
snowflake = Snowflake()

query = snowflake.connection.cursor().execute('Select * From prod_db.public.v_okta_account_changes').fetchall()

for row in query:
    if row[0] == 'ADD EMPLOYEE':
        okta.CreateUser(row[3], row[2], row[4], row[5] if row[5] is not None else '', row[1])
    elif row[0] == 'DELETE EMPLOYEE':
        okta.DeleteUser(row[4])
    elif row[0] == 'UPDATE EMPLOYEE':
        okta.UpdateUser(row[1], row[3], row[2], row[4], row[5] if row[5] is not None else '')