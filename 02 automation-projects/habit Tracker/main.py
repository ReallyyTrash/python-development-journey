import requests
import os
from datetime import date, datetime
from dotenv import load_dotenv

load_dotenv()
pixela_endpoint = "https://pixe.la/v1/users"
token = os.getenv("PIXELA_TOKEN")
user_params = {
    "token": token,
    "username": "reallyytrash",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = "https://pixe.la/v1/users/reallyytrash/graphs"
graph_param = {
    "id": "graph1",
    "name": "Coding",
    "unit": "commit",
    "type": "int",
    "color": 'shibafu',
}
header = {
    'X-USER-TOKEN': token
}
# graph_response = requests.post(url=graph_endpoint, json=graph_param, headers=header)
# print(graph_response.text)
today = datetime(year=2025, month=6, day=12)
foramted_date = today.strftime("%Y%m%d")

pixel_endpoint = "https://pixe.la/v1/users/reallyytrash/graphs/graph1/today"
pixel_para = {
    # "date": foramted_date,
    # "quantity": "1",
    "returnEmpty": True
}

pixel_posting = requests.get(pixel_endpoint, json=pixel_para, headers=header)
print(pixel_posting.text)
