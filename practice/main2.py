from mysql import connector
import tkinter as tk

connection = connector.connect(
    host="192.168.0.104",
    port=3306,
    user="danifanton2",
    password="password",
    database="world"
)

cursor = connection.cursor()

# Read data
cursor.execute("SELECT * FROM city;")
rows = cursor.fetchall()
print("Read",cursor.rowcount,"row(s) of data.")

# Print all rows
for row in rows:
    print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))

window = tk.Tk()

window.mainloop()
