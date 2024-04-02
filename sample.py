import requests
import json

try:
    # Make the GET request to the Rumble API
    api_key = 'XXXXX' # Insert your own API key from https://rumble.com/account/livestream-api
    url = 'https://rumble.com/-livestream-api/get-data?key='
    
    # We need to define the user agent as this is a HTTPS request, if not it fails.
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54'}
    rumble_response = requests.get(url+api_key, headers=headers)
    rumble_data = rumble_response.json()  # Convert the rumble_response to JSON

    # This is the breakdown of how to get to watching now
    # You can examine the details of the API JSON here https://codebeautify.org/jsonviewer
    watching_now = rumble_data["livestreams"][0]["watching_now"]
    
    # Writing the file for OBS to read
    f = open("rumble_watchers_count.txt", "w")
    f.write(str(watching_now))
    f.close()
	
    # Some output for sanity and debug
    print(watching_now, " - Data stored successfully!")
except:
    exit()
