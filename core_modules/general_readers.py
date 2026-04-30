## General Readers
import pandas as pd

dt = None

#%% read spreadsheets with ext detection
def readFile(fp, dtype=dt):
    '''
    Reads CSV or Excel types.
    Detects extension.
    
    Assumes dt as a global parameter.
    dt = partial datatype dict.
    '''
    ext = fp.split('.')[-1].lower()
    
    if 'xls' in ext:
        return pd.read_excel(fp, dtype=dtype)
    
    if ext=='csv':
        return gen_read_csv(fp, dtype=dtype)
            
    #- if prior lines didn't return, invalid file type like *.doc.
    raise Exception('Unhandled file type.')


#%% read csvs w sep detection    
def gen_read_csv(fp, dtype=dt, sep=None):
    """
    Read CSV and infer delimiter by counting characters in first row.
    delims (, ; |)
    """
    if not sep:
        with open(fp, "r", encoding="utf-8", errors="ignore") as f:
            header = f.readline()

        delims = ',;|'
        counts = {d: header.count(d) for d in delims}
        sep = max(counts, key=counts.get)

    return pd.read_csv(fp, sep=sep, dtype=dtype)


#%% test
# =============================================================================
# fd = '../util/static data/'
# 
# wi = readFile(fd+'wi.xlsx')
# wi.shape
# 
# tmo = readFile(fd+'tmobile.csv')
# tmo.shape
# =============================================================================
