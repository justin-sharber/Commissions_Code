##  Package Preamble

#%%  Timer
from time import time, sleep
time0 = round(time())


#%%  Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import date
from glob import glob

import os
from os import mkdir
from os.path import isfile, isdir


#%% Tests
pd.Series(np.arange(5, 10))
date(2021, 5, 15)


#%% Basic vars
today = date.today().strftime('%m-%d')
