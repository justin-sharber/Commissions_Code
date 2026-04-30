## shorten
import pandas as pd

# =============================================================================
# def shorten(s, num=2):
#     '''Shortens a phrase to 'num' terms.'''
#     return ' '.join(s.split(' ')[:num])
# =============================================================================

def shorten(s, num=2):
    '''
    Shortens a phrase to 'num' terms.
    Recursive, overloaded.
    '''  
    if type(s)==pd.Series:
        return s.map(lambda x: shorten(x, num))
    
    elif type(s)==list:
        return [shorten(t, num) for t in s]
    
    elif type(s)==str:
        return ' '.join(s.split(' ')[:num]) 
    
    else:
        print('Incompatible data type.')
        return None
    

s = 'WALT OXLEY ENTERPRISES INC'
shorten(s)