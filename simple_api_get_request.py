#pip install requests
import requests
import json

def get_kanye_rest_quote(self, api):
    response = requests.get(f"{api}")
    print(response.status_code)
    if response.status_code == 200:
        print("sucessfully fetched the data")
        self.formatted_print(response.json())
    else: print(f"Hello, there's a {response.status_code} error with your request")



# API status codes
# 200: Everything went okay, and the result has been returned (if any).
# 301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
# 400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
# 401: The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.
# 403: The resource you’re trying to access is forbidden: you don’t have the right perlessons to see it.
# 404: The resource you tried to access wasn’t found on the server.
# 503: The server is not ready to handle the request.

# def get_data(self, api):
#     response = requests.get("https://api.kanye.rest/")
#     if response.status_code == 200:
#         print("sucessfully fetched the data")
#         self.formatted_print(response.json())
#     else:
#         print(f"Sorry, there's a {response.status_code} error with your request")

#get_kanye_rest_quote()

