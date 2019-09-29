import seaborn as sns
import pandas as pd
from tsfresh.feature_extraction import extract_features,feature_calculators
#from tsfresh import extract_features
from tsfresh.feature_extraction.settings import ComprehensiveFCParameters
from tsfresh.feature_extraction.settings import MinimalFCParameters
from tsfresh.utilities.dataframe_functions import make_forecasting_frame
from sklearn.ensemble import AdaBoostRegressor
from tsfresh.utilities.dataframe_functions import impute
import warnings
warnings.filterwarnings('ignore')

#%matplotlib inline
#%load_ext autoreload
#%autoreload 2
settings_time = MinimalFCParameters()
#settings_time
def feature_extraction(df):
    import pandas as pd
    X_tsfresh = extract_features(df, column_id="id", column_value="value",
                                 default_fc_parameters=settings_time)
    #df = X_tsfresh
    #df =df.T
    #df2.replace(to_replace='value__agg_linear_trend__f_agg_"max"__chunk_len_', value='linear', regex=True)




    
    return X_tsfresh