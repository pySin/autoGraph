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
    
    
    # Get the frequency results for a range bin from a column. Example: How many countries have life expectancy between 61 and 70 years.
    def query_bin(self, single_range):

        query = '''
        SELECT COUNT(%s) AS 'column' FROM %s
        WHERE %s BETWEEN %s AND %s;
                ''' % (self.column_name, self.table_path, self.column_name, single_range[0], single_range[1])

        conn = mysql.connector.connect(host='localhost', user='root',
                                       password='dance')  # MySQL connection.
        cursor = conn.cursor()
        cursor.execute(query)
        bins_life_e = cursor.fetchall()
        cursor.close()
        conn.commit()

        # print(bins_life_e[0][0])
        return bins_life_e[0][0]


# Plot the results of the SQL querying. Create a bar graph with the frequencies for each bin of the range of the column. 
class PlotResults:

    def __init__(self, array_1, array_2):
        self.array_1 = array_1
        self.array_2 = array_2

        
# Now we have both lists ready for a normal Matplotlib plotting. 'array_1' are the graph labels and 'array_2' are the values.
class PlotResults:

    def __init__(self, array_1, array_2):
        self.array_1 = array_1
        self.array_2 = array_2

    def plot_s(self):
        plt.bar(self.array_1, self.array_2)
        plt.show()


# Call the functions in their proper order so the auto-analysis and the graphics appear correctly. 
def call_functions(table_path, column_name, bin_number):
    query_sql = QuerySQL(table_path, column_name, bin_number)

