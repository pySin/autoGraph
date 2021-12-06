# autoGraph. Create a graph from SQL query automatically.
import mysql.connector
import re
import math


# Create a class for the functions that query MySQL and retreive results.
class QuerySQL:

    def __init__(self, table_path, column_name, bin_number):
        self.table_path = table_path
        self.column_name = column_name
        self.bin_number = bin_number

    def min_max_range(self):

        query = '''
        SELECT MIN(%s) AS MIN, MAX(%s) AS MAX FROM %s;
        ''' % (self.column_name, self.column_name, self.table_path)

        conn = mysql.connector.connect(host='localhost', user='root',
                                       password='dance')  # MySQL connection.
        cursor = conn.cursor()
        cursor.execute(query)
        min_max = cursor.fetchall()
        cursor.close()
        conn.commit()

        print(min_max)
        return min_max


def call_functions():
    pass
