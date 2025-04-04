# IN THIS LESSON I LEARNED ABOUT PATH PARAMETERS
from fastapi import FastAPI

app = FastAPI()

# Base url
@app.get('/')
def index():
    return {'data' : 'Blog list'}


# This will return all the unpublised blogs
@app.get('/blogs/unpublished')
def unpublished():
    return {'data' : 'unpublished blogs list'}


# this will return the blog of the id that will be provided by the user
@app.get('/blogs/{id}')
def blog_detail(id :int): # this int insures that the id is a integer.
    return {'blog' : id}




# this will return the comments of blog of the id that will user ask for.
@app.get('/blogs/{id}/comments')
def show_comments(id :int):
    return {'Comments' : {
        '1' : 'First comment',
        '2' : 'Second comment',
        'blog id' : id
    }}