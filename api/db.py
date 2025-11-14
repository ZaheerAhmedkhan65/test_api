import mysql.connector
from mysql.connector import pooling
import os
from dotenv import load_dotenv

load_dotenv()

dbconfig = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "database": os.getenv("DB_NAME"),
    "port": os.getenv("DB_PORT")
}

connection_pool = pooling.MySQLConnectionPool(
    pool_name="product_pool",
    pool_size=5,
    pool_reset_session=True,
    **dbconfig
)

def get_connection():
    return connection_pool.get_connection()
