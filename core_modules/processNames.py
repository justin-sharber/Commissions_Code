from dropDelimiters import *
from cleanTerms import *

def processNames(series, stripSpaces=False):
    '''
    Wrapper function for cleaning customer names.
    '''
    s = series
    s = s.str.upper()
    s = dropDelimiters(s)
    s = cleanTerms(s)
    
    if stripSpaces:
        s = s.str.replace(' ', '')
    
    return s

