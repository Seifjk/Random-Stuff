from scipy.io import arff
import pandas as pd

from periodicity.autocorrelation import autocorrelation

from umwandlung.umwandlung import umwandlung
from featureextraction.tsfresh_extract import feature_extraction


#%matplotlib inline

data = arff.loadarff(r"C:\Users\srfzx\Downloads\ECG5000\ECG5000_TRAIN.arff")
df = pd.DataFrame(data[0])
for i in range(1, len(df)):
    df['id'] = 1

col2 = 'att1'

df2 = pd.DataFrame({"id": df.id.values,
                       "value": df[col2].values
})
df2 = autocorrelation(df2)
print(df2.head(5))
dfextract = feature_extraction(df2)

def freeze_support():
    '''
    Check whether this is a fake forked process in a frozen executable.
    If so then run code specified by commandline and exit.
    '''
    if sys.platform == 'win32' and getattr(sys, 'frozen', False):
        from multiprocessing.forking import freeze_support
        freeze_support()



