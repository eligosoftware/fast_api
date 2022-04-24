import imp
from multiprocessing.spawn import import_main_path
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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