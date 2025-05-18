import requests

url = "http://127.0.0.1:5000/predict"  
data = [
    {
        "Gender": "Male",
        "Age": 25,
        "Height": 175,
        "Weight": 70,
        "Duration": 30,
        "Heart_Rate": 120,
        "Body_Temp": 36.5
    },
    {
        "Gender": "Female",
        "Age": 30,
        "Height": 160,
        "Weight": 60,
        "Duration": 45,
        "Heart_Rate": 130,
        "Body_Temp": 37.0
    }
]

response = requests.post(url, json=data)

if response.ok:
    predictions = response.json()
    for i, result in enumerate(predictions['predicted']):
        print(f"User {i+1} => Predicted Calories: {result['Calories']}")
else:
    print("Error:", response.text)
