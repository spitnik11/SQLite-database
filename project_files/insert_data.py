import os
import sqlite3
# using pandas module
import pandas.io.sql as sql


# run to insert table data

def main():
    # Connecting to sqlite using custom path relative to user
    # (copy and paste path from db folder to troubleshoot)
    start = "/Users/losth/OneDrive/Desktop/Final_Project/db/help_desk_service_request.db"
    # make path absolute
    absolute_p = os.path.abspath(start)
    database = absolute_p
    conn = sqlite3.connect(database)

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # delete all rows from table
    cursor.execute('DELETE FROM REQUESTS;', )

    # define 3 rows to be inserted into REQUESTS table
    cursor.execute('''INSERT INTO REQUESTS(  
    id, date_of_request, description_of_request, technician_assigned, date_of_completion, notes) VALUES 
    (1, '7-1-21', 'Create database for final', 'Gabriel Pina', '7-19-21', 'use sqlite with python')''')

    cursor.execute('''INSERT INTO REQUESTS(
    id, date_of_request, description_of_request, technician_assigned, date_of_completion, notes) VALUES 
    (2, '7-2-21', 'Create video instructions', 'Gabriel Pina', '7-19-21', 'use obs')''')

    cursor.execute('''INSERT INTO REQUESTS(
    id, date_of_request, description_of_request, technician_assigned, date_of_completion, notes) VALUES 
    (3, '7-3-21', 'Export database', 'Gabriel Pina', '7-19-21', 'use sqlite csv command')''')

    # Commit your changes in the database
    conn.commit()
    print("Records inserted........")

    # Closing the connection
    conn.close()


main()
