from datetime import datetime
from dotenv import load_dotenv
import requests, os
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

host_domain = "https://trackapi.nutritionix.com"
exercise_endpoint = '/v2/natural/exercise'
url_exercise = f"{host_domain}{exercise_endpoint}"

APP_ID = os.getenv("NT_APP_ID")
API_KEY = os.getenv("NT_API_KEY")

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

spreadsheet_endpoint = os.getenv("SHEET_ENDPOINT")
token = os.getenv("SHEET_TOKEN")
headers_sheet = {
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
    sheet_response = requests.post(spreadsheet_endpoint, json=sheet_inputs, headers=headers_sheet)
    print(sheet_response.json())
