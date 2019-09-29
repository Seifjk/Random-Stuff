from scipy.signal import find_peaks
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from scipy.signal import find_peaks
#peaks, _ = find_peaks(autocorr, height=0)
def autocorrelation(df):
    s = pd.Series(df.value)
    autocorr = [s.autocorr(lag=i) for i in range(2,100)]
    #pd.plotting.autocorrelation_plot(dfum.value);
    peaks, _ = find_peaks(autocorr, height=0)
    #dfum.index = pd.to_datetime(df.Datetime)
    #plt.plot(dfum.index[peaks[1]:peaks[2]+1], dfum.value[peaks[1]:peaks[2]+1
    #'Datetime2': df.index[peaks[1]:peaks[2]+1]
    
    d = {'value': df.value[peaks[1]:peaks[2]+1]}
    dffinal = pd.DataFrame(data=d)
    for i in range(1,len(df)):
        dffinal['id'] = 1
        plt.plot(dffinal.value)
    return dffinal
    