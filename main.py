from connector import param
from readfromtable.readfromtable import readfromtable

#import umwandlung

tablename = input("Input Tablename: ")
col1 = input("Input Column Name: ")
col2 = input("Input Column Name: ")
startId = input("Input Start ID: ")
endId = input("Input End ID: ")
df = readfromtable(tablename,col1, col2, startId, endId)
df.head()
#dfum = umwandlung(df, col2)
#autocorrelation(dfum)

#df = normalize(0.03, df, col2)
#df.head()
#df['HYD_Hochdruck'] = df['HYD_Hochdruck'].apply(lambda x: x*0.03)
#for i in range(1,len(df)):
#df['id'] = 1
k=input("press close to exit")