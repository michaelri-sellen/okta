# Sellen Construction / Okta API integration

To use this script, you will need Python 3 installed and an API key generated from Okta (see [this link](https://developer.okta.com/docs/guides/create-an-api-token/create-the-token/) for instructions on generating an API token). You will also need to generate a key pair to use the Snowflake connector (see [this link](https://docs.snowflake.net/manuals/user-guide/python-connector-example.html#using-key-pair-authentication)).

- From a command prompt install the requirements: `python3 -m pip install -r requirements.txt`
- Run the test script with Python 3 to generate a config file: `python3 okta_tests.py`
- Enter your configuration information into the config file
- Run the test script again to perform the initial tests
- Once testing is complete, run the initial import script: `python3 initial_import.py`
- The main script can now be run regularly to update Okta with any changes that have been made: `python3 main.py`
