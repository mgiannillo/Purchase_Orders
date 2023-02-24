import pandas as pd



purchase_orders = pd.DataFrame(columns= ['Vendor', 'Type_of_Spend', 'Brand','PO_Number', 'PO_Amount',
                                         'Invoice_Amount', 'Difference', 'Date_Opened'], index = range(0,5000))

import random as random

import time

import datetime as datetime

def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.
    
    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """
    
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    
    ptime = stime + prop * (etime - stime)
    
    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y', prop)




vendors = ['Disney Studios',
           'Google Inc.',
           'Meta Platforms',
           'KYG Antler LLC',
           'The Martingale Agency',
           'TikTok Inc',
           'Nintendo Technologies',
           'Pinterest Inc']

spend_types = ['Brand Publicity', 
               'Influencer',
               'Media Supported Asset',
               'Brand Asset Development', 
               'E-Commerce']

brands = ['Space Wars',
          'Clay-Dough',
          'Transmorphers',
          'Merf',
          'GI-Bro']

purchase_orders = pd.DataFrame(columns= ['Vendor', 'Type_of_Spend', 'Brand','PO_Number', 'PO_Amount', 
                                         'Invoice_Amount', 'Difference', 'Date_Opened'], index = range(0,5000))

purchase_orders['Vendor'] = [random.choice(vendors) for item in purchase_orders['Vendor']]

purchase_orders['Type_of_Spend'] = [random.choice(spend_types) for item in purchase_orders['Type_of_Spend']]

purchase_orders['Brand'] = [random.choice(brands) for item in purchase_orders['Brand']]

purchase_orders['PO_Number'] = [random.randint(10000000,99999999) for item in purchase_orders['PO_Number']]

purchase_orders['PO_Amount'] = [random.randint(200,100000) for item in purchase_orders['PO_Amount']]

purchase_orders['Invoice_Amount'] = [random.randint(0,item) for item in purchase_orders['PO_Amount']]

purchase_orders['Date_Opened'] = [random_date('01/01/2022','12/30/2022', random.random()) for item in purchase_orders['Date_Opened']]

purchase_orders['Date_Opened'] = pd.to_datetime(purchase_orders['Date_Opened'],format='%m/%d/%Y')

purchase_orders['Invoice_Amount'] = [random.randint(0,item) for item in purchase_orders['PO_Amount']]


Q1_start = '01/01/2022'
Q1_end = '03/31/2022'
Q2_start = '04/01/2022'
Q2_end = '06/30/2022'
Q3_start = '07/01/2022'
Q3_end = '09/30/2022'
Q4_start = '10/01/2022'
Q4_end = '12/31/2022'



Q1 = (purchase_orders['Date_Opened'] >= Q1_start) & (purchase_orders['Date_Opened'] <= Q1_end)
Q2 = (purchase_orders['Date_Opened'] >= Q2_start) & (purchase_orders['Date_Opened'] <= Q2_end)
Q3 = (purchase_orders['Date_Opened'] >= Q3_start) & (purchase_orders['Date_Opened'] <= Q3_end)
Q4 = (purchase_orders['Date_Opened'] >= Q4_start) & (purchase_orders['Date_Opened'] <= Q4_end)


purchase_orders.loc[Q3, 'PO_Amount'] = purchase_orders['PO_Amount'] + 25000

purchase_orders.loc[Q4, 'PO_Amount'] = purchase_orders['PO_Amount'] + 50000

purchase_orders['Difference'] = purchase_orders['PO_Amount'] - purchase_orders['Invoice_Amount']

purchase_orders = purchase_orders.sort_values('PO_Amount', ascending = False)

print(purchase_orders['PO_Amount'][Q1].sum())

print(purchase_orders['PO_Amount'][Q4].sum())

purchase_orders.to_csv('C:/Users/mgian/Desktop/PO_Data.csv')


