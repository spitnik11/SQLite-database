import os
import sqlite3


# run to create database tables


def main():
    start = "/Users/losth/OneDrive/Desktop/Final_Project/db/help_desk_service_request.db"
    # make path absolute
    absolute_p = os.path.abspath(start)

    # Connecting to sqlite using custom path
    # (copy and paste path from db folder to troubleshoot)
    database = absolute_p
    conn = sqlite3.connect(database)

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Dropping REQUESTS table if already exists.
    cursor.execute("DROP TABLE IF EXISTS REQUESTS")

    # Creating table as per requirements from instructor
    sql = '''CREATE TABLE REQUESTS(
    id integer PRIMARY KEY,
    date_of_request text NOT NULL,
    description_of_request text NOT NULL,
    technician_assigned text NOT NULL,
    date_of_completion text NOT NULL,
    notes text NOT NULL          
    )'''
    # Execute cursor object
    cursor.execute(sql)
    print("Table created successfully........")

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()


main()
