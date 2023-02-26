## Purchase Orders Analysis Part One: Simulating the Data

#Step 1: Import Necessary packages

import pandas as pd

import random as random

import time

import datetime as datetime

#Step 2: Define necessary formulas 

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
  

#Step 4: Define lists of values to simulate observations from

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

#Step 5: Create empty purchase_orders DataFrame with custom column headers and dimensions

purchase_orders = pd.DataFrame(columns= ['Vendor', 'Type_of_Spend', 'Brand','PO_Number', 'PO_Amount', 
                                         'Invoice_Amount', 'Difference', 'Date_Opened'], index = range(0,5000))

#Step 6: Populate columns of purchase_orders DataFrame

##Populate Vendor columns with random selection of items from the vendors list created in Step 4

purchase_orders['Vendor'] = [random.choice(vendors) for item in purchase_orders['Vendor']]

##Populate Type_of_Spend columns with random selection of items from the spend_types list created in Step 4

purchase_orders['Type_of_Spend'] = [random.choice(spend_types) for item in purchase_orders['Type_of_Spend']]

##Populate Brand columns with random selection of items from the brands list created in Step 4

purchase_orders['Brand'] = [random.choice(brands) for item in purchase_orders['Brand']]

##Populate PO_Number columns with random number between 1,000,000 and 9,999,999 to assign a 6 digit identifier code to each observation

purchase_orders['PO_Number'] = [random.randint(10000000,9999999) for item in purchase_orders['PO_Number']]

##Populate PO_Amount column with random integer between 200 and 100,000 to simulate the price of each purchase order observation

purchase_orders['PO_Amount'] = [random.randint(200,100000) for item in purchase_orders['PO_Amount']]

##Populate the Invoice Amount column with a random integer between 0 and the value in the PO_Amount column for that row.

purchase_orders['Invoice_Amount'] = [random.randint(0,item) for item in purchase_orders['PO_Amount']]

##Use random_date formula to generate a random date in the year 2022 to assign a a date to each observation. Formate date to mm/dd/yyyy.

purchase_orders['Date_Opened'] = [random_date('01/01/2022','12/30/2022', random.random()) for item in purchase_orders['Date_Opened']]

purchase_orders['Date_Opened'] = pd.to_datetime(purchase_orders['Date_Opened'],format='%m/%d/%Y')

#Step 7: Simulate a rise in costs through year-end

##Establish Date ranges for Q1,Q2,Q3,Q4
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

##For each observation that fits the criteria in the Q3 and Q4, add 25,000 or 50,000 respectively to the PO Amount value.

purchase_orders.loc[Q3, 'PO_Amount'] = purchase_orders['PO_Amount'] + 25000

purchase_orders.loc[Q4, 'PO_Amount'] = purchase_orders['PO_Amount'] + 50000

##Step 8: Calculate Difference columns by subtracting Invoice_Amount from PO_Amount

purchase_orders['Difference'] = purchase_orders['PO_Amount'] - purchase_orders['Invoice_Amount']

##Step 9: Test to see if prices rise throughout the year

print(purchase_orders['PO_Amount'][Q1].sum())
print(purchase_orders['PO_Amount'][Q2].sum())
print(purchase_orders['PO_Amount'][Q3].sum())
print(purchase_orders['PO_Amount'][Q4].sum())

##Step 10: Export as CSV for SQL Analysis and Tableau Dashboard creation

purchase_orders.to_csv('PO_Data.csv')


