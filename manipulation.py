import sqlite3
from PyQt5.QtWidgets import QMessageBox

conn = sqlite3.connect('stock.db')

c = conn.cursor()

def insert_prod(name,q,cost, minQ, date):
    print ('insert function')
    with conn:
        c.execute("SELECT quantity FROM stock WHERE name = :name",{'name':name})
        check = c.fetchone()

    print(check)
    if check is None:
        with conn:
            print('yes')
            c.execute("INSERT INTO stock VALUES (:name, :quantity, :cost, :minQuantity)", {'name': name, 'quantity': q, 'cost': cost, 'minQuantity': minQ})
            print('values inserted')
            a = name.upper() +' ' +str(q)+' '+str(cost)+' '+str(minQ) +' '+str(date) + ' ' + 'INSERT '+"\n"
            print(a)
            with open("transaction.txt", "a") as myfile:
                myfile.write(a)
        return 'Inserted the stock in DataBase'
    else:
        return 'Stock with same name already present.'

def show_stock():
    with conn:
        c.execute("SELECT * FROM stock")

    return c.fetchall()


def update_cost(name, cost,date):
    with conn:
        c.execute("""UPDATE stock SET cost = :cost
                    WHERE name = :name""",
                  {'name': name, 'cost': cost})


def update_quantity(name, val, date):
    #print ('entering update_quantity')
    with conn:
        c.execute("SELECT quantity FROM stock WHERE name = :name",{'name': name})
        z = c.fetchone()
        #print(z)
        cost = z[0]+val
        #print(cost)
        if cost < 0:
            return
        c.execute("""UPDATE stock SET quantity = :quantity
                    WHERE name = :name""",
                  {'name': name, 'quantity': cost})
        #print('executed')
        a = name.upper() + ' ,old quantity:' + str(z[0]) + ' ,new quantity:' + str(cost) + ' ' + str(date) +' UPDATE '+"\n"
        #print(a)
        with open("transaction.txt", "a") as myfile:
            myfile.write(a)
        #print('hello')
        #-------------------minimum quantity alert-------------------
        c.execute("SELECT minQuantity FROM stock WHERE name = :name", {'name': name})
        mq=c.fetchone()
        #print(mq)
        msg=int(mq[0])
        print('msg=' , int(msg))
        print('cost= ', int(cost))
        if (cost < msg)or (cost == msg):
            return True
            
            #messagebox.showinfo('Alert', 'Minimum Quantity Reached. Please re-order now')

            #QMessageBox.about(self, "Alert", "Minimum Quantity Reached. Please re-order now.")
            #QtWidgets.QMessageBox.warning(self, 'Alert', 'Minimum Quantity Reached. Please re-order now.')
            #print('Minimum Quantity Reached. Please re-order now.')
        


def remove_stock(name,date):
    with conn:
        c.execute("DELETE from stock WHERE name = :name",
                  {'name': name})
        a = name.upper() + ' ' + 'None' + ' ' + 'None'+' ' + str(date) + ' REMOVE '+"\n"

        with open("transaction.txt", "a") as myfile:
            myfile.write(a)

        conn.commit()

#-------------------------------------
#def show_stock():
#    with conn:
#        c.execute("SELECT * FROM stock")

#    return c.fetchall()


#conn.close()
