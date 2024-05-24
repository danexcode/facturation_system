from database.connection import Connection

db_service = Connection.get_instance()

class Order():
    def __init__(self):
        pass
    
    def enough_stock(self, products):
        for product in products:
            amount = product[2]
            stock = product[3]
            if stock - amount < 0:
                return False
        return True
    
    
    def insert_order(self, order):
        """
        order = {
            products: [(id, price, amount, stock)], 
            total = 200$,
            client_id: 1
        }
        """
        
        if not self.enough_stock(order["products"]):
            raise ValueError("No hay suficientes productos")
        
        connection = db_service.get_connection()
        cursor = connection.cursor()
        
        total = order["total"]
        client_id = order["client_id"]
        order_values = (total, client_id)
        sql = "INSERT INTO orders (total, client_id) VALUES (%s,%s)"
        
        cursor.execute(sql, order_values)
        connection.commit()
        
        order_id = cursor.lastrowid
        products = order["products"]
        
        sql = "INSERT INTO order_product (order_id, product_id, amount, product_price) VALUES (%s,%s,%s,%s)"
        for product in products:
            product_id = product[0]
            price = product[1]
            amount = product[2]
            order_values = (order_id, product_id, amount, price)
            cursor.execute(sql, order_values)
            connection.commit()
            cursor.execute(
                "UPDATE products SET stock = stock - %s WHERE id = %s",
                (amount, product_id)
            )
            connection.commit()
            
    