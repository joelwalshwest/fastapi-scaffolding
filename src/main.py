from fastapi import FastAPI
import debugpy
import requests


debugpy.listen(("0.0.0.0", 5678))

app = FastAPI()


@app.get("/")
def read_root():
    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=GOOG&apikey=T80PZJVLGVP3IVN7"
    r = requests.get(url)
    data = r.json()
    price = data["Global Quote"]["05. price"]
    return "Current Goog  price is: " + price
