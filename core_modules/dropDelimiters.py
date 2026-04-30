import pandas as pd

def dropDelimiters(s):
    """
    Removes delimiters from a pandas Series.
    """
    delims = '\'",./|;'
    for delim in delims:
        s = s.str.replace(delim, '')
    return s


#%% test
# =============================================================================
# s = ['"Mr." White', 'separator/| city;',]
# s = pd.Series(s)
# dropDelimiters(s)
# =============================================================================

