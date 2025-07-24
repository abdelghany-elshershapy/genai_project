from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def count_ages():
    # __define-ocg__: Start of the age filtering logic
    varOcg = requests.get("https://coderbyte.com/api/challenges/json/age-counting")
    
    # Get the data string
    data_string = varOcg.json().get("data", "")
    
    # Split the string by comma and clean spaces
    items = [item.strip() for item in data_string.split(",")]

    # Extract ages
    varFiltersCg = []
    for i in range(0, len(items), 2):  # every two items: key, age
        if "age=" in items[i+1]:
            age_value = int(items[i+1].split("=")[1])
            if age_value >= 50:
                varFiltersCg.append(age_value)

    return {"count": len(varFiltersCg)}

