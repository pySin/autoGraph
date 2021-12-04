# autoGraph. Create a graph from SQL query automatically.
import mysql.connector
import re
import math


class GetResults:
    def query_1(self): # path of the table, name of the column, number of bins wanted.
        query = '''
        SET @sixth = ROUND((((SELECT MAX(LifeExpectancy) FROM world.country) 
			                 - (SELECT MIN(LifeExpectancy) FROM world.country))/6), 2); 
        SELECT @sixth;
        SELECT COUNT(LifeExpectancy) FROM world.country
        WHERE LifeExpectancy BETWEEN (SELECT MIN(LifeExpectancy) + @sixth*0 FROM world.country) AND
							         (SELECT MIN(LifeExpectancy) + @sixth*2 FROM world.country);
        '''


def call_functions():
    pass
