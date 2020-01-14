from okta_api import Okta

okta = Okta()

# Run API tests with a test user and the API functions above
#testUser = {
#    'firstName': 'DNU',
#    'lastName': 'DoNotUse',
#    'email': 'SellenTeam@gmail.com',
#    'phone': '+1-206-795-3158',
#    'eid': '00001'
#}

testUser = {
    'firstName': 'test',
    'lastName': 'michael',
    'email': 'michaelri.sellen@gmail.com',
    'phone': '+1-212-555-1212',
    'eid': '99999'
}

okta.CreateUser(testUser['firstName'], testUser['lastName'], testUser['email'], testUser['phone'], testUser['eid'])
print('Press enter to continue or Ctrl + C to quit')
input()
okta.UpdateUser(testUser['eid'], '', '', '', '')
print('Press enter to continue or Ctrl + C to quit')
input()
okta.DeleteUser(testUser['email'])