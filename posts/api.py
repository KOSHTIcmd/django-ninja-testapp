from ninja import NinjaAPI
from django.http import HttpRequest

posts = [
    {
        "id":1, 
        "title":"title 1", 
        "content":"content 1" 
    },
    {
        "id":2, 
        "title":"title 2", 
        "content":"content 2" 
    },
    {
        "id":3, 
        "title":"title 3", 
        "content":"content 3" 
    }
]

api = NinjaAPI()

@api.get('/')
def test(request:HttpRequest):
    return {'message': 'Hello SHUBH'}

@api.get('/add')
def add(request:HttpRequest, x:int, y:int):
    return {"result":(x+y)}

@api.get('/post/{posy_id}')
def get_post_by_id(request:HttpRequest, post_id:int):
    for post in posts:
        if post["id"] == post_id:
            return post
        
    return {"error":"Not Found"}
