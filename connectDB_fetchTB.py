import sqlite3
def search(name2):
    con = sqlite3.connect('TEST.db')
    cursor = con.cursor()
    sql = '''
           SELECT * FROM CUSTOMER WHERE NAME = ?
          '''
    try:
        cursor.execute(sql,[name2])
        record = cursor.fetchall()
        return record
    except:
        print('Unable to fetch data as you are not registered.')

print("Fetch worked")
