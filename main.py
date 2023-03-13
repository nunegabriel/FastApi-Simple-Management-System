from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get('/greet/{name}')
def great_name(name:str):
    return {"greetings":f"Hello {name} "}