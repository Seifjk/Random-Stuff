
from readfromtable.readfromtable import readfromtable
from umwandlung.umwandlung import umwandlung
from periodicity.autocorrelation import autocorrelation
from featureextraction.tsfresh_extract import feature_extraction
from writetotable.writetotable import write_to_table

import pandas as pd
#import umwandlung




def main():
 tablename = input("Input Tablename: ")
 col1 = input("Input Column Name: ")
 col2 = input("Input Column Name: ")
 startId = input("Input Start ID: ")
 endId = input("Input End ID: ")
 table_name = input("Insert Table Name :")

 df = readfromtable(tablename,col1, col2, startId, endId)





 for i in range(1,len(df)):
         df['id'] = 1
 df2 = umwandlung(df, col2)
 df3 = autocorrelation(df2)

 dfextract = feature_extraction(df3)

 write_to_table(dfextract, table_name)

 #pd.plotting.autocorrelation_plot(df.value);
 print(dfextract.head())
 #dfum = umwandlung(df, col2)
 #autocorrelation(dfum)



if __name__ == "__main__":
    main()