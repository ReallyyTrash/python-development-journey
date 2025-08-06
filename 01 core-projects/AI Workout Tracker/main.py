import requests, os
from datetime import datetime

app_id = "8c47af76"
api_key = "833aa7ea685034e3960ab4452b700073"

host_domain = "https://trackapi.nutritionix.com"
exercise_endpoint = '/v2/natural/exercise'
url_exercise = f"{host_domain}{exercise_endpoint}"

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameter = {
    "query": str(input("What was acheived today?")),
    "weight_kg": 69,
    "height_cm": 177,
    "age": 18,
}

response = requests.post(url_exercise, headers=headers, json=parameter)
result = response.json()
# print(result)

spreadsheet_endpoint = "https://api.sheety.co/6345ce058d753cb5ab0cc05218250a9d/workoutTracker/sheet1"
token = "adslkfjadslkgjkjhgkjdfhsg"
headers = {
    "Authorization": f"Bearer {token}"
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(spreadsheet_endpoint, json=sheet_inputs, headers= headers)
    print(sheet_response.json())
