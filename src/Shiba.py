import requests
import webbrowser

# Define a variable with the URL of the API
api_url = "http://shibe.online/api/shibes?count=1"

# Call the root of the api with GET, store the answer in a response variable
# This call will return a list of URLs that represent dog pictures
response = requests.get(api_url)

# Get the status code for the response. Should be 200 OK
# Which means everything worked as expected
print(f"Response status code is: {response.status_code}")

# Get the result as JSON
response_json = response.json()

url = str(response_json)
url = url.replace('[', '')
url = url.replace(']', '')
url = url.replace("'", "")

webbrowser.open(url)