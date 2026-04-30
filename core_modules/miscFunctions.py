## Data Functions
'''
My auxiliary functions.
'''

#%% Packages
import pandas as pd
import numpy as np

#%% getMode
def getMode(L):
    '''
    Easy way to get the mode of a list L.  
    Use with apply (on full columns), or groupby-agg(getMode).
    '''
    if len(L) == 0:
        return None
    s = pd.Series(L).value_counts()
    return s.index[0]

# =============================================================================
# m = getMode([1, 2, 2, 3]); print(m)
# m = getMode([]); print(m)
# =============================================================================

#%% glance
def glance(df):
    '''
    See the head with the last few columns.
    '''
    cols = list(df.columns[:1]) + list(df.columns[-3:])
    return df[cols].head()


#%% misc
def money(num):
    '''
    Number in money format.
    I use this like once in C2-Merged Checks.  
    >> series.map(money)
    '''
    return "${:,.0f}".format(num)


def beep():
    '''
    - beep -
    '''
    os.system('\a')
