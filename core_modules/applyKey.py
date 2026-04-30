## Apply Key

#%% Packages
import pandas as pd


## FUNCTIONS ----
#%%  applyKey
def applyKey(df, keyPath, create=True):
    """
    Reads and applies a column key.
    
    Parameters:
        df (DataFrame): Input data
        keyPath (str): Path to column key file
        create (bool): Whether to create missing columns
    """
    # Load key as series with orignal names as index.
    k = pd.read_excel(keyPath, index_col='Old').New
    # Drop blank rows.
    k = k[k.index.notnull()]
    
    #- handle columns that appear in the column key, but not original data.
    if create:  
        #- Add new columns as blanks to the df
        newCols = [col for col in k.index if col not in df.columns]
        df[newCols] = pd.NA
    else:  
        #- Remove unmatched columns from key.  
        cols = [col for col in k.index if col in df.columns]
        k = k[cols]         
        
    # Slice and order columns.
    df = df[k.keys()].copy()
    # Rename columns - only where new names exist.
    df = df.rename(columns=k.dropna())
    
    return df

#%% Test
# =============================================================================
# from compPaths import *
# 
# fp = dataFolder+'wi.xls'
# wi = pd.read_excel(fp)
# kp = keyFolder+'wiKey.xlsx'
# wi = applyKey(wi, kp).head()
# print(wi.dtypes.head(10))
# =============================================================================
