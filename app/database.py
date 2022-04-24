import imp
from multiprocessing.spawn import import_main_path
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
import psycopg2
from psycopg2.extras import RealDictCursor

#SQL_ALCHEMY_DATABASE='postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
SQL_ALCHEMY_DATABASE='postgresql://postgres:root@localhost/fastapi'

engine=create_engine(SQL_ALCHEMY_DATABASE)

session_local=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db =session_local()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',
#         password='root',cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Successfully connected to database")
#         break
#     except Exception as error:
        
#         print("Connection to database has failed :(. Error: ",error)
#         time.sleep(2)