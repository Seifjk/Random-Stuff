import pandas as pd
import seaborn as sns
from tsfresh.feature_extraction import extract_features,feature_calculators
#from tsfresh import extract_features
from tsfresh.feature_extraction.settings import ComprehensiveFCParameters
from tsfresh.feature_extraction.settings import MinimalFCParameters
from tsfresh.utilities.dataframe_functions import make_forecasting_frame
from sklearn.ensemble import AdaBoostRegressor
from tsfresh.utilities.dataframe_functions import impute


def umwandlung(df, col2):
   # col2= input("Input Column Name: ")
    #col2 = input("Input Column Name: ")
    df = pd.DataFrame({"id": df.id.values, 
                       "value": df[col2].values
                       #"value2": df.col2.values,


                    },
                       index=pd.DatetimeIndex(
                           df.Datetime
                       ))
    return df