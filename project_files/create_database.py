import os
import sqlite3
from sqlite3 import Error

# run to create database connection

# define connection method using db_file as argument for custom path
start = "/Users/losth/OneDrive/Desktop/Final_Project/db/help_desk_service_request.db"
# make path absolute
absolute_p = os.path.abspath(start)


def create_connection(db_file):
    # create a database connection to a SQLite database
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def main():
    create_connection(absolute_p)


main()
# define path to store database
# (copy and paste path from db folder to troubleshoot)
