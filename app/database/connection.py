import mysql.connector

class Connection():
    _instance = None
    port = 3306
    host = "192.168.0.104"
    database = "tienda"
    connection = None
    def __init__(self):
        raise RuntimeError("This is a Singleton, use get_instance() instead.")

    
    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = cls.__new__(cls)
        return cls._instance
        
    
    def connect(self, username="", password=""):
        if username and password:
            self.username = username
            self.password = password
        self.connection = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password,
            database=self.database
        )
        return self.connection
    
    def get_connection(self):
        return self.connection
    
    def get_cursor(self):
        con = self.connect()
        cursor = con.cursor()
        return cursor
    