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
    "port": int(os.getenv("DB_PORT", 4000)),  # TiDB Cloud default MySQL port is usually 4000
    "ssl_disabled": False,                    # enable SSL
    "ssl_verify_cert": False                  # same as rejectUnauthorized: false
}

# Connection pool
connection_pool = pooling.MySQLConnectionPool(
    pool_name="tidb_pool",
    pool_size=10,
    pool_reset_session=True,
    **dbconfig
)

def get_connection():
    """Get a connection from the TiDB pool"""
    return connection_pool.get_connection()
