import requests 
from datetime import datetime as dt 

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "ishanr1"
TOKEN = "eyvedvqlqeyge2764vdkkdhbdieh"
# randomly generated 
GRAPHID = "graph2"
GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/"
ADD_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPHID}"


PARAMETERS = {
    "token": "eyvedvqlqeyge2764vdkkdhbdieh",
    "username": "ishanr1",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

GRAPH_PARAMS = {
    "id": GRAPHID,
    "name": "Workout Graph",
    "unit": "Pump",
    "type": "int",
    "color": "momiji"
}


today = dt.now()

PIXEL_PARAMS = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create a user
# response = requests.post(url=PIXELA_ENDPOINT, json=PARAMETERS)
# print(response.text)

# Create a graph 
# response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_PARAMS, headers=headers)
# print(response.text)

# Add a pixel
response = requests.post(url=ADD_PIXEL_ENDPOINT, json=PIXEL_PARAMS, headers=headers)
print(response.text)

# a system where users get nnotified every day to record their activity and that gets stored as a pixel 


