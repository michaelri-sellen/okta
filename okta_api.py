#This script makes API calls to the Okta API
# It requires the urls, header, and PrettyPrint() from the Common script
import json, requests
from common import Common

common = Common() #Create a new instance of the Common class. This gives access to PrettyPrint()
config = common.okta_config #This gives access to the urls and header

class Okta:
    #This function creates a new user in Okta
    # When calling CreateUser(), the firstName, lastName, email, phone, and eid are required
    # A password is not required, but if one is provided a welcome email will not be sent to the user
    def CreateUser(self, firstName, lastName, email, phone, eid, password = None):
        #Build the data structure using the parameters that were passed to CreateUser()
        data = {
        'profile': {
            'firstName': firstName,
            'lastName': lastName,
            'email': email,
            'mobilePhone': phone,
            'login': email,
            'employeeNumber': eid
            },
        'groupIds': [config.group_id]
        }
        if password is not None:
            data['credentials'] = {
                'password': {
                    'value': password
                }
            }
        data = json.dumps(data) #Format the data structure for use with the Okta API

        #Call the Okta API using the formatted data and store the response from the API
        response = requests.post(config.users_url, data = data, headers = config.headers)
        
        if response.ok: #User was created successfully
            print("User {} has been added".format(email))
            #Now that the user has been created, provision the E-Toolbox app to them
            self.__AddToEToolbox(json.loads(response.text)['id'], email)
        else: #User was not created, PrettyPrint() the error message
            common.PrettyPrint(response.text)

    #This function is private and can only be called by other functions in this class
    # It will provision the E-Toolbox app to the userID specified
    def __AddToEToolbox(self, userID, email):
        #Build the data structure using the parameters that were passed to __AddToEToolbox()
        data = {
            'id': userID,
            'scope': 'USER',
            'credentials': {
                'userName': email,
                'password': {}
            }
        }
        data = json.dumps(data) #Format the data structure for use with the Okta API

        #Call the Okta API using the formatted data and store the response from the API
        response = requests.post(config.apps_url + config.app_id + '/users', data = data, headers = config.headers)

        if response.ok: #E-Toolbox was provisioned successfully
            print('E-Toolbox was assigned to the account {}'.format(email))
        else: #E-Toolbox was not provisioned, PrettyPrint() the error message
            common.PrettyPrint(response.text)

    #This function deletes the specified user
    def DeleteUser(self, user):
        #Send the delete request for the specified user and store the status_code
        # The first time the delete request is submitted, the account is disabled but not deleted
        # The second time the delete request is submitted, the account is fully deleted
        # When the status code is 404, the user could not be found
        status = requests.delete(config.users_url + user, headers=config.headers).status_code
        while status != 404: #Keep sending the delete request until the user can no longer be found
            status = requests.delete(config.users_url + user, headers=config.headers).status_code
        print('User {} has been deleted'.format(user))
    
    #This function will update the information for the specified user. It uses the eid to identify the specific user to update
    def UpdateUser(self, eid, firstName, lastName, email, phone):
        #Find the user by searching for their eid via the Okta API
        get_user = requests.get(config.users_url + '?search=profile.employeeNumber+eq+"{}"'.format(eid), headers = config.headers)
        
        if get_user.ok: #The get user request was successful
            #Store the ID of the user so that the updates are applied to the right person
            user = json.loads(get_user.text)[0]['id']

            #Build the data structure using the parameters that were passed to UpdateUser()
            data = {
                'profile': {
                    'firstName': firstName,
                    'lastName': lastName,
                    'mobilePhone': phone,
                    'login': email,
                    'email': email,
                }
            }
            data = json.dumps(data) #Format the data structure for use with the Okta API

            #Call the Okta API using the formatted data and store the response from the API
            response = requests.post(config.users_url + user, data = data, headers = config.headers)

            if response.ok: #The user was updated successfully
                print('The update to user {} was successful'.format(eid))
            else: #The user was not updated, PrettyPrint() the error message
                common.PrettyPrint(response.text)
        else: #The get user request was not successful, PrettyPrint() the error message
            common.PrettyPrint(get_user.text)