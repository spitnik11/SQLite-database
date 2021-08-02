import os
import sqlite3
# using pandas module
import pandas.io.sql as sql
from sqlite3 import Error


# exports data to csv file which can be viewed in microsoft excel
# Connecting to sqlite

# database connection
# (copy and paste path from db folder to troubleshoot)
def main():
    start = "/Users/losth/OneDrive/Desktop/Final_Project/db/help_desk_service_request.db"
    # make path absolute
    absolute_p = os.path.abspath(start)
    database = absolute_p
    conn = sqlite3.connect(database)
    try:
        # read in table and rows
        table = sql.read_sql('select * from REQUESTS', conn)
        # Export data into CSV file
        table.to_csv(r'C:\Users\losth\OneDrive\Desktop\Final_Project\REQUESTS_DATA.csv', index=False)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


main()
