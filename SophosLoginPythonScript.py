import requests
import sys
import getpass
import time

def submit_request_with_credentials(url, username, password, req="login"):
    #current_state = "signed_in" if check_network_connection() else "not_signed_in"

    if req == "login":
        request_data = {
            'mode': '191',
            'username': username,
            'password': password,
            'a': str(int(time.time() * 1000))
        }

        make_requests_request("POST", url+"login.xml", data=request_data)
    else:
        if req == "logout":
            logout_data = {
                'mode': '193',
                'username': username,
                'a': str(int(time.time() * 1000))
            }
            make_requests_request("POST", url+"logout.xml", data=logout_data)

def make_requests_request(method, url, data=None, callback=None):
    try:
        response = requests.request(method, url, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'}, verify=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Handle the response here
        print(response.text)

        if callback:
            callback(response.text)

    except requests.exceptions.RequestException as e:
        # Handle errors here
        print('Error:', e)

if len(sys.argv) > 4 or len(sys.argv)<=2:
    print("Usage: python SophosLoginPythonScript.py <login or logout> <username> <password>")
    sys.exit(1)


url = "https://hfw.vitap.ac.in:8090/"
operation = sys.argv[1]
username = sys.argv[2]
password = ""
if len(sys.argv) == 4:
    password = sys.argv[3]

if sys.argv[1] == "login" or sys.argv[1] == "logout":
    submit_request_with_credentials(url, username, password, sys.argv[1])
else:
    print("Usage: python SophosLoginPythonScript.py <login or logout> <username> <password>")
    sys.exit(1)
