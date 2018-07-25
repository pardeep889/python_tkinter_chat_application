import mysql.connector
# mydb = mysql.connector.connect(
#   host="db4free.net",
#   user="pardeep889",
#   passwd="qwerty@123",
#   database= "pythondatabase_c"
# )
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database= "pythondatabase_chat"
)

def view_data():
    c = mydb.cursor()
    c.execute("SELECT Name,Message FROM data_table WHERE Status = 1 ORDER BY id DESC")
    rows = c.fetchall()
    return (rows)
