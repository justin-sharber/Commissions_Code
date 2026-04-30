## Balances
def calcBalance(summary): 
    '''
    Loads balance ledger.  
    Combines previous balance with current net commission.
    Calculates according and exports new ledger.

    Parameters
    ----------
    summary : df
        Summary of commission calcluations.
        
    '''
    # load
    fp = utilFolder+'balances.xlsx'
    bal0 = pd.read_excel(fp).set_index('Agent')
    #- Overwrite current month if rerunning.
    if month in bal0.columns:
        bal0 = bal0.drop(columns=month)

    balances = bal0.copy()
    
    # active balances are the right-most month in ledger.
    cols = balances.columns[[0, -1]]
    balances = balances[cols]
    
    # input prior balance, set up columns
    c = balances.columns[-1]
    summary['PriorBalance'] = balances[c]
    summary['ActBalance'] = balances.loc[idx, c]
    summary['ActPayment'] = 0

    #- assume positive, pay total
    tot = summary.NetActComp + summary.ActBalance
    summary['ActPayment'] = tot
    summary['ActBalance'] = 0

    #- flip on negatives
    idx = tot<0
    summary.loc[idx, 'ActPayment'] = 0
    summary.loc[idx, 'ActBalance'] = tot

    #- calc balances
    summary['NewBalance'] = summary.ActBalance + summary.ResBalance
    summary['Payment'] = summary.ActPayment + summary.ResPayment

    #- store and export balance ledger
    new = summary.NewBalance
    bal0[month] = new
    bal0.to_excel(fp)
    bal0.to_excel(backupFolder+'balance backup - {}.xlsx'.format(today))

    return(summary)