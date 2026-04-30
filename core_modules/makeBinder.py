## makeBinder
import pandas as pd

def makeBinder(fp, reportDict, keepIndex=False):
    '''
    Uses ExcelWriter to create a spreadsheet with multiple tabs.
    reportDict: {'Report Name': df}
    '''
    with pd.ExcelWriter(fp, engine='xlsxwriter') as writer:   
        for name in reportDict.keys():
            s = reportDict[name]
            ind = keepIndex | (type(s)==pd.Series)
            s.to_excel(writer, sheet_name=name, index=ind, startrow=2)
            writer.sheets[name].write_string(0, 0, name)
    
    fn = fp.split('/')[-1]
    print('Exported:', fn)            
    return None


#%% test
# =============================================================================
# s1 = pd.Series([1,2,3])
# s2 = pd.DataFrame([4,5,6])
# reportDict = {
#     'Report A': s1,
#     'Report B': s2,}
# fp = 'C:/Users/Werk/Docs/test report.xlsx'
# makeBinder(fp, reportDict)
# =============================================================================

