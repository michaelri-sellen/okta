from okta_api import API

okta = API()

# Run API tests with a test user and the API functions above
testUser = {
    'firstName': 'test',
    'lastName': 'michael',
    'email': 'michaelri.sellen@gmail.com',
    'phone': '+1-206-555-1212',
    'eid': '99999'
}

okta.CreateUser(testUser['firstName'], testUser['lastName'], testUser['email'], testUser['phone'], testUser['eid'])
print('Press enter to continue or Ctrl + C to quit')
input()
okta.UpdateEmail(testUser['email'], 'test@example.com')
print('Press enter to continue or Ctrl + C to quit')
input()
okta.DeleteUser(testUser['email'])