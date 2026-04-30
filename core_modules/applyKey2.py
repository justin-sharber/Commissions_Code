# -*- coding: utf-8 -*-
"""
applyKey2
@author: Justin

An enhancement of applyKey.  
Allows for multiple column aliases in the source.
Also allows for unused renaming entries.
This was necessary for multiple data sources that significantly changed format and we needed to read both.

"""

import pandas as pd

def applyKey2(df, keyPath):
    '''
    Applies a column key to a df.
    Splits renaming columns from slicing the df.
    Distinguishes between required columns.
    Required columns throw an error if not present.
    
    Brilliantly checks if there is a rename sheet,
      which defines aliases for columns.
    '''
    #- rename - usually necessary but optional.
    xls = pd.ExcelFile(keyPath)
    if 'rename' in xls.sheet_names:
        r = pd.read_excel(keyPath, index_col='Old', sheet_name='rename').New
        r = r.to_dict()
        df = df.rename(columns=r)
    
    #- key
    k = pd.read_excel(keyPath, index_col='Col', sheet_name='slice')
    k = k[k.index.notna()]
    #- bool
    k.Required = (k.Required==1)
    
    #- enforce required cols
    idx = k.Required
    missing = [c for c in k[idx].index if c not in df.columns]
    if missing:
        assert False, 'Missing required columns: \n{}'.format(missing)
        
    #- spam unmatched
    idx = ~k.Required
    newCols = [c for c in k[idx].index if c not in df.columns]
    df[newCols] = pd.NA
    
    #- slice
    df = df[k.index]
    
    return df
    
    
        
        
