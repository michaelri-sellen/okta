from openpyxl import load_workbook
from okta_api import API

okta = API()
source = list(load_workbook('OKTA Query from Snowflake.xlsx', read_only=True).worksheets[0].rows)

for row in range(1, len(source)):
    okta.CreateUser(source[row][2].value, source[row][1].value, source[row][3].value, source[row][4].value, source[row][0].value)