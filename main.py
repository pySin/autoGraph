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
    
    # Calculate the bin size for the column we chose and the number of bins. Make a list with all the bin ranges.
    def calculate_bins(self, min_value, max_value):
        values_range = max_value - min_value
        bin_size = round(values_range / self.bin_number, 2)

        bins_all = []

        for n_of_bins in range(self.bin_number):
            bins_all.append([min_value, min_value + bin_size])
            min_value = min_value + bin_size

        return bins_all


def call_functions():
    pass
