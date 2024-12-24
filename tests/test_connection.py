import pytest
import sqlite3
import os

def test_connection():
    """
    Python pytest
    ---
    Params: No arguments/parameters
    Objetive: Test if it is possible to connect to the database
    """
    assert __import__('sqlite3')
    path_ = os.path.join(os.path.dirname(__file__), '..\\scripts_module\\data\\CarSalesData.db')

    connection = sqlite3.connect(path_)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Clients")
    assert type(cursor.fetchall()) is list

    connection.commit()
    cursor.close()

test_connection()