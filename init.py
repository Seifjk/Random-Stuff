import mysql.connector
from sklearn import preprocessing
from scipy.signal import find_peaks
from mysql.connector import Error
import sqlalchemy
import mysql.connector
import pandas.io.sql as psql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tsfresh.feature_extraction import extract_features,feature_calculators
#from tsfresh import extract_features
from tsfresh.feature_extraction.settings import ComprehensiveFCParameters
from tsfresh.feature_extraction.settings import MinimalFCParameters
from tsfresh.utilities.dataframe_functions import make_forecasting_frame
from sklearn.ensemble import AdaBoostRegressor
from tsfresh.utilities.dataframe_functions import impute