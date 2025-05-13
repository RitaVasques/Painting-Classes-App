from mysql.connector import pooling
from mysql.connector import Error

class ConnectDB:
    DATABASE = 'PaintingStudio_students_db'
    USERNAME = 'root'
    PASSWORD = '' # insert password
    DB_PORT = '3307'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'painting_pool'
    pool = None

    @classmethod
    def get_pool(cls): 
        if cls.pool is None: # Create object pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f'Error getting pool: {e}')
        else:
            return cls.pool

    @classmethod
    def getConnection(cls):
        return cls.get_pool().get_connection()
    
    @classmethod
    def freeConnection(cls, connect_db):
        connect_db.close()