import requests

# IP address of the Starlink router
url = 'http://192.168.1.1/api/v1/system/advanced/WiFiPassword'

# Send request to the router
response = requests.get(url)

# Print the Wi-Fi password
print(response.json()['password'])
