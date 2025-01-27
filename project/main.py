from fastapi import FastAPI # Import the FastAPI class from the fastapi module
from pydantic import BaseModel # Import the BaseModel class from the pydantic module
app = FastAPI() # Create a FastAPI instance

class Custom(BaseModel):
    name: str
    age: int
    address: str
# the app instance is the main part of our FastAPI application. Used to configure the application altogether.
# / means the root path of the application (the socket-address of the application) 
@app.get("/ping") # Decorator (@app) to define the path of the endpoint
async def root():
    return {"message" : "Hello World!!!!"}

@app.get("/")
async def root():
    return {"Info" : "This is Anshuman Bhardwaj"}
@app.get("/blog/comments")
async def read_comments():
    return {"comments" : "No comments yet"}

# @app.get("/blog/{blog_id}")
# async def read_blog(blog_id: str,q : str = None,name : str = "Anshuman"):
#     print(q,name)
#     return {"blog_id" : blog_id}

@app.post("/blog/{blog_id}")
async def read_blog(blog_id: int,request_body: Custom ,q : str = None ):
    print(request_body.name)
    print(q)
    return {"blog_id" : blog_id,"q" : q}
# http://127.0.0.1:8000/blog/25?key=anshuman : after ? is query params
#query params are optional and are used for filteration 
