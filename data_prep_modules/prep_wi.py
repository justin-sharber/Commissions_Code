## Prep WI
from loadCoreModules import *
from prepBoolCols import prepBoolCols
from setDeviceType import setDeviceType


#%% process / format

def processWI(wi0):
    '''
    Processes WI data.  
    Applies key, applies data types, etc.
    Slices down to Closed-Won and IOT lines,
      since I want that for both commissions & KPI (more stable).
    '''
    #- don't mutate the original.
    wi = wi0.copy()
    
    keyPath = keyFolder+'wiKey.xlsx'
    wi = applyKey(wi, keyPath)

    #- columns
    wi.Customer = processNames(wi.Customer)
    wi.BAN = wi.BAN.str.replace(' ', '')
        
    k = {'Partner-Generated': 'PG','Teamed': 'DL'}
    wi.SellType2 = wi.SellType.map(k)
    
    #- dates
    wi.Date = wi.Date.fillna(wi.ActDate)
    wi['Month'] = wi.Date.astype(str).str[:7]  

    #- bools
    wi = prepBoolCols(wi)
                 
    #- IOT
    wi['IOT'] = wi.IOT | wi.Customer.str.upper().str.contains('SONITROL')
    wi.loc[wi.IOT, 'CorePlan'] = wi.CorePlan.fillna(5)
    
    #- Models
    wi['DeviceType'] = setDeviceType(wi.Model)
    wi.Model = shorten(wi.Model, 3)
    
    #- Routers -    
    routerTerms = ['Router','Cradlepoint', 'Peplink', 'Pepwave', ]
    for term in routerTerms:
        wi['Router'] = wi.Router | wi.Model.str.title().str.contains(term)
    wi['Router'] = wi.Router & ~wi.Model.str.upper().str.contains('BYOD')
    
    #- Comp info
    wi.QuantityConfirmed = wi.QuantityConfirmed.replace(0, np.nan)
    wi.Qty = wi.QuantityConfirmed.fillna(wi.Qty)
    
    wi['MRC'] = wi.CorePlan.fillna(0) + wi.Addons.fillna(0)
    wi['LineMRC'] = wi.MRC
    wi['OrderMRC'] = wi.Qty * wi.MRC
    
    #- cleanup
    dropCols = [
        'MRC', 
        'CorePlan', 
        'Addons', 
        'QuantityConfirmed', 
        ]
    wi = wi.drop(columns=dropCols)
    
    cols = ['Customer', 'Month']
    wi = wi.sort_values(by=cols)#.drop(columns=dropCols)
    
    wi['in_wi'] = True
    
    return wi


#%% Prep
fp = filepaths.loc['wi'].Filepaths[-1]
wi0 = readFile(fp, dt)
wi = processWI(wi0)
wi.shape
