from fastapi import FastAPI
import debugpy


debugpy.listen(("0.0.0.0", 5678))

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "world"}
