from openpyxl import load_workbook
from okta_api import API
from enum import Enum

okta = API()
source = list(load_workbook('OKTA Query from Snowflake.xlsx', read_only=True).worksheets[0].rows)

for row in range(1, len(source)):
    First = source[row][2].value
    Last = source[row][1].value
    Email = source[row][3].value
    Phone = source[row][4].value
    Eid = source[row][0].value

    Phone = Phone if Phone is not None else ''

    okta.CreateUser(First, Last, Email, Phone, Eid)
    print("Created  {}: {} {} - {} - {}".format(Eid, First, Last, Email, Phone))