import sqlalchemy
import numpy as np
import pandas as pd
import mysql.connector



def write_to_table(df, table_name):
    database_username = 'root'
    database_password = 'Zangetsu10'
    database_ip       = 'localhost'
    database_name     = 'feldbuslogging'
    database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                   format(database_username, database_password, 
                                                          database_ip, database_name))
    df.to_sql(con=database_connection, name=table_name , if_exists='replace')