#!/usr/bin/env python
# coding: utf-8

# In[73]:


#Подключаем необходимые библиотеки
def gasessions():
    import json
    import sqlite3
    import pandas as pd
    import glob


    # In[82]:


    import pandas as pd
    import glob

    path = './'
    all_files = glob.glob(path + "/ga_sessions_new*")

    li = []

    for filename in all_files:
        with open(filename, 'r') as j:
            contents = json.load(j)
        contents



    for l in contents.values():
       print(l[0])


    # In[85]:


    for l in contents.values():
        new_df = pd.DataFrame(l)


    # In[86]:


    new_df.info()


    # In[87]:


    li.append(new_df)
    frame1 = pd.concat(li, axis=0, ignore_index=True)


    # In[89]:


    frame1.info()


    # In[90]:


    from sqlite3 import Error

    def sql_connection():

        try:

            con = sqlite3.connect('mydatabase.db')

            return con

        except Error:

            print(Error)

    # def sql_table(con):

    #     cursorObj = con.cursor()

    #     cursorObj.execute("CREATE TABLE gahits(id integer PRIMARY KEY, session_id text, hit_date date, hit_time text, hit_number integer, hit_type text, hit_referer text, hit_page_path text, event_category text, event_action text, event_label text, event_value text)")
    #     con.commit()

    con = sql_connection()
    # sql_table(con)


    # In[91]:


    frame1.to_sql('gasessions', con, if_exists='replace', index=False)


# In[ ]:
if __name__ == '__main__':
    gasessions()




