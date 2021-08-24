import sqlite3;
import pandas as pd;

from contextlib import closing;
conn = sqlite3.connect("C:\\Users\\tbels\\OneDrive\\Documents\\SDCCE\\Python for DB\\DBs_for_SQLite\\Assignment4\\customers.sqlite")

a_file = open("C:\\Users\\tbels\\OneDrive\\Documents\\SDCCE\\Python for DB\\DBs_for_SQLite\\Assignment4\\customers.csv")
rows = pd.read_csv(a_file)

with closing(conn.cursor()) as cursor:
    query = "DELETE FROM Customer"
    cursor.execute(query)
    conn.commit()

rows.columns = ['firstName', "lastName", "companyName", "address", "city", "province", "postal"]
rows.to_sql('Customer', conn, if_exists='append', index=False)
conn.commit()


# Close connection
if conn: 
    conn.close();