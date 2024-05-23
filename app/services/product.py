from database.connection import Connection

db_service = Connection.get_instance()

class Product():
    def __init__(self):
        pass
        
    def get_products_names(self):
        #try:
        connection = db_service.get_connection()
        cursor = connection.cursor()
        #cursor.execute("CALL get_products_names();", multi=True)
        cursor.execute("SELECT name FROM products")
        rows = cursor.fetchall()
        names = []
        for row in rows:
            names.append(row[0])
        print(names)
        return names
        #except:
            #print("Ocurrio un error")

    def get_product(self, product):
        connection = db_service.get_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM products WHERE name="{product}"')
        rows = cursor.fetchone()
        return rows
