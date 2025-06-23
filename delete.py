import sqlite3

from sqlite3 import Error

def delete():
    def sql_connection():
        try:

            con = sqlite3.connect('mydatabase.db')

            return con

        except Error:

            print(Error)

    def sql_table(con):
        cursorObj = con.cursor()

        cursorObj.execute("DELETE FROM gahits")
        cursorObj.execute("DELETE FROM gasessions")
        con.commit()


    con = sql_connection()
    sql_table(con)
