import mysql.connector
from mysql.connector import Error
mydb = mysql.connector.connect(host='localhost',
                                        database='feldbuslogging',
                                         user='root',
                                         password='Zangetsu10',
				auth_plugin='mysql_native_password')