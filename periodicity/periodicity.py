import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
sns.set()
plt.figure(figsize=(15, 6))
plt.plot(dfum.index, dfum.value)
plt.xlabel('Datetime', fontsize=20)
plt.ylabel('HYD_Hochdruck', fontsize=20);
plt.show()