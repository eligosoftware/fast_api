from fastapi import  FastAPI
import time
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine
from .routers import post,user,auth


models.Base.metadata.create_all(bind=engine)

app=FastAPI()



while True:
    try:
        conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',
        password='root',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Successfully connected to database")
        break
    except Exception as error:
        
        print("Connection to database has failed :(. Error: ",error)
        time.sleep(2)



my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},
        {"title":"title of post 2   ","content":"content of post 2","id":2}
        ]



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Welcome to my API"}






