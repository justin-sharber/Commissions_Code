## Set Device type
from loadCoreModules import *

def setDeviceType(model):
    '''
    Outputs series of device types.
    '''
    fp = utilFolder+'device types.xlsx'
    device = pd.read_excel(fp)
    device.DeviceType = device.DeviceType.fillna(device.Term)
    device = device.set_index('Term').DeviceType

    model = model.str.lower()
    device.index = device.index.str.lower()
    
    s = pd.Series(pd.NA, index=model.index)
    
    for term in device.index:
        idx = model.str.contains(term)
        s[idx] = device[term]
        #print(term, idx.sum())
    
    return s
        
        
        