from packages import *

def export(df, index=False):
    '''    
    Exports a df to "Downloads/chex.xlsx."
    Used for quick looking / troubleshooting.
    '''
    if type(df) == pd.Series:
        index=True
        
    fd = 'C:/Users/Werk/Downloads/'
    df.to_excel(fd+'chex.xlsx', index=index)
    print('Exported as "chex".')

