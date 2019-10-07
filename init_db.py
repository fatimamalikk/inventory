import sqlite3


#To use sqlite3 module, you must first create a connection object that
#represents the database and then optionally you can create a cursor
#object, which will help you in executing all the SQL statements.



if __name__ == '__main__':

    conn = sqlite3.connect('stock.db')

    c = conn.cursor()


    c.execute("""CREATE TABLE stock (
                name text,
                quantity integer,
                cost integer
                ) """)

    conn.commit()
