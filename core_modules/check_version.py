import sys

def checkVersion():
    '''
    Checks environment and python version.  
    Uses sys.executable & sys.version.
    '''
    envy = sys.executable.split('\\')[-2]
    print('Envio -', envy)
    
    ver = sys.version.split('|')[0].strip()
    print('Python -', ver)
    return ver

checkVersion()
