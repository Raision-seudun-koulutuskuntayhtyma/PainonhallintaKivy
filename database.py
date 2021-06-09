# Database module

# Libraries and modules to import
import sqlite3
from sqlite3.dbapi2 import SQLITE_INSERT

# Create a new database
database_name = 'weightmanagement.db'

def create_db(file):
    """Creates a db, extension must be db

    Args:
        file (string): The name of the database file
    """
    connection = sqlite3.connect(file)
    connection.close()

def create_table(file):
    """Creates tables needed for the database
    """
    # Create the connection to the database
    connection = sqlite3.connect(file)

    # Create the table for measurements
    connection.execute('''CREATE TABLE measure 
        (measure_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        p_height REAL NOT NULL,
        p_weight REAL NOT NULL,
        sex INTEGER NOT NULL,
        age INTEGER NOT NULL);''')
            
    
    # Close the connection after creation of tables
    connection.close()


# Function for creating quoted SQL clause
def sql_string(field):
    field = "'" + field + "'"
    return field

# Routine for adding measurement
def add_measure(file, p_height, p_weight, sex, age):
    """Adds measurement data to measure table

    Args:
        file (string): Name of the database file
        p_height (float): height in cm
        p_weight (float): weight in kg
        sex (integer): coded sex, 1 male, 0 female
        age (integer): age (whole number)
    """
    sql_clause = "INSERT INTO measure ( p_height, p_weight, sex, age) VALUES (" + str(p_height) + "," + str(p_weight) + "," + str(sex) + "," + str(age) + ");"

     # Create a connection to the database
    connection = sqlite3.connect(file)

    # Execute the SQL clause
    connection.execute(sql_clause)

    # Commit the transaction
    connection.commit()

    # Close the connection
    connection.close()


# Paikallinen testaus
if __name__ == "__main__":

    # create_db(database_name)
    create_table(database_name)

    
   