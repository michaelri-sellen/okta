# Sellen Construction / Okta API integration

To use this script, you will need Python 3 installed and an API key generated from Okta (see [this link](https://developer.okta.com/docs/guides/create-an-api-token/create-the-token/) for instructions on generating an API token).

- From a command prompt install the requirements: `python3 -m pip install -r requirements.txt`
- Run the script with Python 3 to generate a config file: `python3 okta_tests.py`
- Enter your API key into the config file
- The script can now be run regularly to make the included API calls to the Okta API.
