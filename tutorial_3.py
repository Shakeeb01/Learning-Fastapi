# IN THIS LESSON I LEARNED ABOUT QUERY PARAMETERS & REQUEST BODY
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


# Base url
@app.get('/')
def index():
    return {'Data':'Blogs'}

# blogs
@app.get('/blogs')
def blogs(limit: int=10, published: bool=True):
    """
    Default value will 10 for the limit query parameter
    and for published it will be True.
    """
    if published == True:
        return {'data' : f'Blog list of {limit} published blogs.'}
    else:
        return {'data' : f'Blog list of {limit} Unpublished blogs.'}




# Model for creating blog
class Blog(BaseModel):
    name: str
    body: str
    published: Optional[bool]

# Url for creating blog
@app.post('/create_blog')
def create_blog(blog: Blog):
    return {'message':'blog is created','data' : blog}
