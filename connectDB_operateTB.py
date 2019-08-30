import sqlite3
def debit(name3, initial_amount):
    con = sqlite3.connect('TEST.db')
    cursor = con.cursor()
    sql = '''
               UPDATE CUSTOMER 
               SET INITIAL_AMOUNT = ?
               WHERE NAME = ?
              '''
    try:
        cursor.execute(sql, [initial_amount,name3])
        con.commit()
    except:
        print('Unable to update data as you are not registered.')

def credit(name3, initial_amount):
    con = sqlite3.connect('TEST.db')
    cursor = con.cursor()
    sql = '''
               UPDATE CUSTOMER 
               SET INITIAL_AMOUNT = ?
               WHERE NAME = ?
              '''
    try:
        cursor.execute(sql, [initial_amount,name3])
        con.commit()
    except:
        print('Unable to update data as you are not registered.')
