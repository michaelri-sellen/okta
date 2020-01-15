#This is the main script that runs weekly
# It grabs all changes since the previous week from Snowflake and performs the appropriate action in Okta
# The columns from Snowflake are ordered as follows:
# 0 = ACTION_TO_TAKE
# 1 = EMPLOYEE (EID)
# 2 = LASTNAME
# 3 = FIRSTNAME
# 4 = EMAIL
# 5 = CELLPHONE
from okta_api import Okta
from snowflake_connection import Snowflake

okta = Okta() #Create a new instance of the Okta class
snowflake = Snowflake() #Create a new instance of the Snowflake class

#Perform the SQL query and store the results
query = snowflake.connection.cursor().execute('Select * From prod_db.public.v_okta_account_changes').fetchall()

for row in query: #Perform each action one row at a time
    if row[0] == 'ADD EMPLOYEE':
        okta.CreateUser(row[3], row[2], row[4], row[5] if row[5] is not None else '', row[1])
    elif row[0] == 'DELETE EMPLOYEE':
        okta.DeleteUser(row[4])
    elif row[0] == 'UPDATE EMPLOYEE':
        okta.UpdateUser(row[1], row[3], row[2], row[4], row[5] if row[5] is not None else '')