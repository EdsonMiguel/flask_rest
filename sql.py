import MySQLdb


host = "localhost"
user= "user_py"
password=""
db = "app_py"
port = 3306


con = MySQLdb.connect(host, user, password, db, port)
c = con.cursor(MySQLdb.cursors.DictCursor)


def select(fields, tables, where=None):
    global c
    query = (f"SELECT {fields} FROM {tables}")    
    if(where):
        query = query + (f' WHERE {where}') 
    c.execute(query)
    return c.fetchall()


print(select("nome, email","usuarios"))
    
