import functools
import pymysql
import pymysql.cursors
from src.config import configuration


@functools.lru_cache(maxsize=100, typed=False)
def get_connection():
    print('Creating engine.')
    db_user = configuration.DB_USERNAME
    db_host = configuration.DB_HOST
    db_pass = configuration.DB_PASSWORD
    db_port = configuration.DB_PORT
    db_name = configuration.DB_NAME
    connection = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_pass,
        port=3306,
        db=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
