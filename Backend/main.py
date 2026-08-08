from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message" : "AegisSOC API is Running"}