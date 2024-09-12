# from fastapi import FastAPI

# app = FastAPI()



# @app.post("/")
# def hellowordl():
#     return "Hello World i'm learning FastAPI-Post!!"

# @app.get("/")
# def hellowordl():
#     return "Hello World i'm learning FastAPI-Get!!"


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}