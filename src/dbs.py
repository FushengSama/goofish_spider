from sqlalchemy.schema import Table
from sqlalchemy import create_engine
import sqlalchemy as sq
user='root'
password='123456'
host='localhost'
port=3306
database='spiderTest'

def init_db()->sq.Engine:
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}',
                       echo=True, pool_recycle=7200, pool_size=5, max_overflow=10, pool_timeout=30)
    return engine
sqlEngine=init_db()
    
