# This is how we run the server
# uvicorn tutorial_1:app --reload
from fastapi import FastAPI


# Creating Instance of the fastapi
app = FastAPI()



@app.get('/') # '/' this is base url
def index():
    return {'data' : {
        'name' : "Shakeeb ur Rehman",
        'age' : 23,
    }}
    # this is how we return json reponse.


@app.get('/about')
def intro():
    return {'about' :"Shakeeb is a backend developer" }