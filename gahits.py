import json
import sqlite3
import pandas as pd
import glob


def gahits() -> object:
    contents_ga_hits_new1 = None
    path = './'
    all_files = glob.glob(path + "/ga_hits_new*")

    li = []

    for filename in all_files:
        with open(filename, 'r') as j:
            contents_ga_hits_new1 = json.load(j)
        print(contents_ga_hits_new1)

    for l in contents_ga_hits_new1.values():
        print(l[0])

    for l in contents_ga_hits_new1.values():
        new_df = pd.DataFrame(l)

        li.append(new_df)
        frame1 = pd.concat(li, axis=0, ignore_index=True)

        frame1.info()

    from sqlite3 import Error

    def sql_connection():

        try:

            con = sqlite3.connect('mydatabase.db')

            return con

        except Error:

            print(Error)

    con = sql_connection()

    frame1.to_sql('gahits', con, if_exists='replace', index=False)


if __name__ != '__main__':
    pass
else:
    gahits()
