import uuid
import json
import re
import time






from sqlalchemy import create_engine, Column, Integer, String,VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import Table
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import CHAR,INTEGER,TEXT,TIME

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:123456@192.168.31.11:3310/spiderTest',
                       echo=True, pool_recycle=7200, pool_size=5, max_overflow=10, pool_timeout=30)
    





class goods():
    def __init__(self,user_name:str,instruction:str,location:str,link:str,category:str,price:int,size:str=None):
        self.category=category
        self.price=price
        self.user_name=user_name
        self.uuid=str(uuid.uuid4())
        self.location=location
        self.size=size
        self.instruction=instruction
        self.link=link
        self.update_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        
    def __str__(self):
        if self.size:
            k={"category":self.category,
                    "price":self.price,
                    "uuid":self.uuid,
                    "location":self.location,
                    "user_name":self.user_name,
                    "size":self.size,
                    "instruction":self.instruction,
                    "link":self.link
                    }
        else:
            k={"category":self.category,
                    "price":self.price,
                    "uuid":self.uuid,
                    "location":self.location,
                    "user_name":self.user_name,
                    "instruction":self.instruction,  
                    "link":self.link
                    }
        return json.dumps(k)

class sqlGoods(Base):
    __tablename__="goods"
    uuid=Column(CHAR(36),primary_key=True)
    price=Column(INTEGER)
    category=Column(CHAR(64))
    location=Column(CHAR(16))
    user_name=Column(CHAR(64))
    instruction=Column(TEXT)
    link=Column(VARCHAR(255))
    update_time=Column(TIME)



if __name__=="__main__":
    a=goods("114",132343125,"adaw","http://baidu.com","daf",1221)
    Session=sessionmaker(bind=engine)
    session=Session()
    session.add(sqlGoods(
        uuid=a.uuid,
        price=a.price,
        category=a.category,
        location=a.location,
        user_name=a.user_name,
        instruction=a.instruction
    ))
    print(a)

    try:
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()