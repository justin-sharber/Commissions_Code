## tmobile functions
from loadCoreModules import *
from load_ban_list import banList


#%% prep tmobile
def processTMobile(tmobile):   
    #- Strip spaces, apply key
    tmobile = tmobile.copy()
    tmobile = joinTerms(tmobile)

    keyPath = keyFolder+'tmobileKey.xlsx'
    tmobile = applyKey(tmobile, keyPath)
           
    #- Columns
    tmobile.Customer = processNames(tmobile.Customer)
    tmobile.BAN = tmobile.BAN.str.replace('S', '')
      
    tmobile['in_tmo'] = True    
    
    for t in ('ALL', 'AJ'): 
        idx = tmobile.CheckNumber.str.contains(t)
        tmobile.loc[idx, 'CheckType'] = t

    #- Qty: +1, -1, 0 from Incoming commission
    tmobile['Qty'] = (tmobile.Incoming / (tmobile.Incoming.abs()+0.0001)).round()
    
    #- attribute Reps
    bl = banList.Rep
    tmobile['Rep'] = tmobile.BAN.map(bl)
    
    sorting = ['Month', 'Customer', 'ActivityType']
    tmobile = tmobile.sort_values(by=sorting)
    
    return tmobile


#%% rundown
def makeRundown(tmobile):
    gCols = ['CheckType', 'Month', 'Customer', 'ActivityType']
    cols = ['Qty', 'Incoming', ]
    tmo = tmobile.groupby(gCols)[cols].sum()
    return tmo


#%% preload
tm0 = read_files_from_list('tmobile'); tmobile0 = tm0;
if type(tm0)==pd.DataFrame:
    tmobile = processTMobile(tm0)
    tmobile.shape
