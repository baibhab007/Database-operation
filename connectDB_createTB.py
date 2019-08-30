import sqlite3


def register(NAME, AGE, SEX, INITIAL_AMOUNT):
    con = sqlite3.connect('TEST.db')
    cursor = con.cursor()
    sql1 = 'DROP TABLE IF EXISTS CUSTOMER'
    sql2 = '''

           CREATE TABLE CUSTOMER (

           NAME CHAR(20) NOT NULL,

           AGE INT,

           SEX CHAR(1),

           INITIAL_AMOUNT FLOAT

           )

          '''
    # cursor.execute(sql1)
    # cursor.execute(sql2)

    rec = (NAME, AGE, SEX, INITIAL_AMOUNT)
    sql = '''

           INSERT INTO CUSTOMER VALUES ( ?, ?, ?, ?)

          '''
    try:
        cursor.execute(sql, rec)
        con.commit()
        print("Thanks for registering.")
    except Exception as e:
        print("Error Message :", str(e))
        con.rollback()
    con.close()
