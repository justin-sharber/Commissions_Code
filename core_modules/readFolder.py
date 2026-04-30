## Read Folder

#%% Packages
from packages import *
      
#%% read folder
def readFolder(fd, reader, ext='csv', subfolders=False):
    '''
    Reads a folder.  Drops duplicates. 
    You can specify it to read one layer of subfolders - non-recursive.
    You must define a reader function each time with only the filepath parameter.
    parameters:
        fd (str): Filepath
        reader (function): Core reader to apply throughout folder
        ext (str): Spreadsheet extension
        subfolders (bool): whether to add one layer of folders below.        
    '''
    files = glob(fd+'*.'+ext)
    
    if subfolders:
        files = files + glob(fd+'*/*.'+ext)
    
    frames = [reader(fp) for fp in files]
    df = pd.concat(frames, ignore_index=True).drop_duplicates()
    
    return df


#%% Test read folder
# =============================================================================
# def reader(fp):
#     return pd.read_csv(fp, sep='|', dtype=str)
# 
# fd = '../input/'
# df = readFolder(fd, reader)
# print(df.shape)
# 
# 
# =============================================================================
