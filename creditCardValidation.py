from datetime import *

def validateCard(expDate):
    if expDate > datetime.now().date():
        print('Valid')
    else:
        print('Expired')

validateCard(date(2018,2,2))