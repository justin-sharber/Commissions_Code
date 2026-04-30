import pandas as pd

def containsAny(series, terms):
    '''
    Returns the series index for containing any terms (iterable)
    '''
    idx = pd.Series(False, series.index)
    for t in terms:
        idx = idx | series.str.contains(t)
        
    return idx

#%% Test
s = ['Mr Simmons', 'Mr Adams', 'Ms Kent']
s = pd.Series(s)
terms = ['Adams', 'Barret', 'Simmons', ]

containsAny(s, terms) 
