## Split Terms, join terms
'''
Splits pascal-case terms into separate words.
Useful for formatting data quickly into readable reports for management.
'''

import pandas as pd

#%% splitTerms
def splitter(txt):
    '''
    Applies splitting and title case to terms, unless they are pure acronyms.
    Should be appropriate for all DF outputs.
    Ex: ActDate -> Act Date
    '''
    txt = txt.replace('_', ' ')
    
    if txt.isupper():
        return txt
    
    txt2 = txt[0].upper() #- initialize, start w capital.
    for i in range(1, len(txt)):
        s = txt[i]
        if txt[i-1].islower() and s.isupper():
            s = ' '+s
        txt2+=s      
    return txt2


def splitTerms(L):
    '''
    Overloaded function based on type - goes all the way down to a string.
    A Series is tricky to do, especially since you have to determine between index & multi-index.

    '''    
    if type(L) == str:
        return splitter(L)
    
    elif type(L) in (list, pd.Index):
        return [splitter(s) for s in L]
    
    elif type(L) == pd.Series:
        return s.map(splitter)
        
    elif type(L) == pd.DataFrame:
        L = L.copy()
        L.columns = splitTerms(L.columns)
        return L
        
    else:
        print('Unsupported input type.')
        print('>>', L)
        return None
    
    #- Scratch
    if type(s.index)==pd.Index:
        s.name = splitTerms(s.index.name)
    type(s.index)==pd.MultiIndex
    s.index.names
    s.name

    
#%% Join Terms
def joinTerms(s):
    '''
    Joins terms to different structures.
    Basically applies s.replace(' ', '') where appropriate.
    '''
    if type(s) == str:
        return s.replace(' ', '')
    
    elif type(s) in (list, pd.Index):
        return [t.replace(' ', '') for t in s]
    
    elif type(s) == pd.Series:
        return s.map(joinTerms)
    
    elif type(s) == pd.DataFrame:
        s.columns = s.columns.str.replace(' ', '')
        return s

#%% Tests 
# =============================================================================
# #- split terms    
# l = ['IT_Bandwidth', 'Marty Berke']    
# s = pd.Series(l)
# x = splitTerms(s)
# 
# #- join terms
# t = ['Not My Problem', 'Not ever']
# t = pd.Series(t)
# t = pd.DataFrame(columns=t)
# t.loc[0] = 0
# t = joinTerms(t)
# =============================================================================



