from sqlite3 import connect
def dump():
    disk_db = connect('mydatabase.db')
    dump_db = connect('my1.db')
    disk_db.backup(dump_db)
    disk_db.close()
    dump_db.close()
