import mysql.connector
import pandas.io.sql as psql
import pandas as pd

mydb = mysql.connector.connect(host='localhost',
                               database='feldbuslogging',
                               user='root',
                               password='++++++')


def readfromtable(tablename, col1, col2, startId, endId):
    mycursor = mydb.cursor()
    # tablename = input("Input Tablename: ")
    # col1 = input("Input Column Name: ")
    # col2 = input("Input Column Name: ")

    # startId = input("Input Start ID: ")
    # endId = input("Input End ID: ")
    # mycursor.execute(
    #  "SELECT {col} FROM {tbl} WHERE id>=%s AND id<%s".format(
    #      col=colNames, tbl=tablename
    #   ),
    #   (startId, endId)
    # )
    query = "SELECT {col1}, {col2} FROM {tbl} WHERE id>={start} AND id<{end}".format(col1=col1, col2=col2,
                                                                                     tbl=tablename, start=startId,
                                                                                     end=endId)
    return psql.read_sql(query, con=mydb)
