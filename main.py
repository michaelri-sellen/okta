# This code has been written as a placeholder until the database setup has been completed.
# Once the database is set up properly, this code will almost cetainly change to reflect the correct query structure.
from okta_api import Okta
from snowflake_connection import Snowflake

okta = Okta()
snowflake = Snowflake()

#for user in database.connection.cursor("Select * From New_Users").fetchall():
#    api.CreateUser(user[0], user[1], user[2], user[3], user[4])
#
#for user in database.connection.cursor("Select * From Delete_Users").fetchall():
#    api.DeleteUser(user[0])