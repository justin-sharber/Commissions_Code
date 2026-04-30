## Clean Terms
import pandas as pd

badTerms = ['amp;', '&nbsp;', 
    ]

badSuff = ['INC',  'LLP', 'LTD', 'CORP','PLLC', 'LLC', 
    ]

def cleanTerms(series):
    '''
    Cleans glitch terms like 'amp;'.
    Removes irrelevant suffixes such as INC.
    Suffixes are done carefully b/c "inc" can exist in a customer name.
    Does not require upper case.
    '''   
    s = series
    for term in badTerms:
        s = s.str.replace(term, '')    
        s = s.str.replace(term.upper(), '')
       
    for suff in badSuff:
        i = len(suff)
        idx = s.str[-i:].str.upper() == suff
        s[idx] = s.str[:-i]
        
    s = s.str.rstrip()
    
    return s


