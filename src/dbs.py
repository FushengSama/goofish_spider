from sqlalchemy.schema import Table
from sqlalchemy import create_engine
import sqlalchemy as sq
import yaml
import os
def getConfigFromYaml(_path:str=""):
    path=os.path.abspath(_path)
    with open(path,'r',encoding="utf-8") as configFile:
        s=yaml.safe_load(configFile)
        print(type(s))
        return s
k=getConfigFromYaml("./dbconfig.yaml")

print(k)

user=k["user"]
password=["passwd"]
host=["host"]
port=["port"]
database=["database"]

def init_db()->sq.Engine:
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}',
                       echo=True, pool_recycle=7200, pool_size=5, max_overflow=10, pool_timeout=30)
    return engine
sqlEngine=init_db()
    
