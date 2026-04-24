### Note to self - ignore 
**Each project README should clearly answer:**

Problem: What are you solving?

Why it matters: Business or real-world relevance

Approach: Methods/models used

Results: Metrics, insights, visuals

Tech stack: Python, pandas, sklearn, etc.

# Commissions Code

# The Task [Overview]
This project is a full code system for processing commissions.  The problem posed was how to calculate commissions reliably for a  business that activated sets of wireless lines for businesses.  The home business was paid commissions by major wireless carriers, and paid out commissions to sales representatives and independent dealers. The main tasks were:

* Incoming commission payments needed to be matched to home records and analyzed.
* Missing / underpaid commissions needed to be disputed.
* Seller commissions needed to be calculated and reported.

Commission data was spread across multiple statement types that could involve multiple statements per month.

# The System
At the time, we had no data engineer or general working database.  A code system needed to be constructed that could mimic a database in retrieving, merging, processing, and storing data.  Spreadsheets needed to be reliably processed and formatted for multiple different purposes - a single notebook would not "cut it."

My solution was a code system in Python using pandas that would simulate a database and code system.  The code had three tiers: general modules, data-specific processing modules, and task-oriented Jupyter Notebooks at the top level.

## Tier 1: Core Modules
The core modules group consisted of utility and "helper" functions that were used frequently, or relied on in all data prep modules.  The core modules set was loaded at the start of every task notebook, so I could use them in any task.

For example, the module `dropDelimters.py` defined a function that drops delimiters from a series, useful for cleaning customer name fields.

**dropDlimiters.py**
```
import pandas as pd

def dropDelimiters(s):
    '''
    Drops delimiters from series s.
    '''
    delims = '\'",./|;'    
    for delim in delims:
        s = s.str.replace(delim, '')
    return s
```

## Tier 2: Data Prep Modules
Data prep modules processed each data input source.  Each input was sliced, reorganized, and processed with basic information that would always be useful.  In other words, this tier created an effective "silver layer" of data for calculations.

With multiple, heterogeneous data sources, which went through changes in format or updates with some frequency, easy maintenance and transparency was critical.  My solution was a system of **column keys**, in addition to the `applyKey()` function which applied them.  "Column keys" are my invention - they are spreadsheets that define which columns should be included, the order in which they should appear, and which should be renamed.

For example, the *actDetailKey* defines column changes for the carrier Activation Detail Report.  It renames the "SubscriberName" column more clearly as "Customer", and places it first in the column order.

The `applyKey()` function was Key to preparing data. 

```
def applyKey(df, keyPath, create=True):
    '''
    Reads and applies a column key.
    create param - whether to create cols not in the original df.
    Column keys can have blank rows for organization.    
    '''        
    k = pd.read_excel(keyPath, index_col='Old').New
    #- Drop blank rows, which can be used to organize the key.
    k = k[k.index.notnull()]
    
    #- handle columns that appear in the column key, but not original data.
    if create:  
        #- Add new columns as blanks to the df
        newCols = [col for col in k.index if col not in df.columns]
        df[newCols] = pd.NA
    else:  
        #- Remove unmatched columns from key.  
        cols = [col for col in k.index if col in df.columns]
        k = k[cols]         
        
    #- Slice columns - takes all columns listed in the key.
    df = df[k.keys()].copy()

    #- Rename relevant columns, choosing with dropna().
    df = df.rename(columns=k.dropna())
    
    return df
```


(more topics)
# The Incoming Data

#Topics

## apply key
## calc balance
## 
