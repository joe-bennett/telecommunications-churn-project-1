

#Here we are going to import the library basics that will allow our acquisition file to operate properly. Pandas allows us to interact with DataFrames, import os will allow us to interact via python with our operating system directly, 
# and env file is where host name, username, and password is stored and the function that uses that to link the SQL database to our jupyter notebook. 

import pandas as pd
import os
from env import username, password, host


#below is where the function that establishes link to the SQL database. you will need to copy your env.py file into same directory as this file so that it can pull your own credentials to access the codeup SQL database


def get_db_url(db_name):
    return f'mysql+pymysql://{username}:{password}@{host}/{db_name}'

telco_connnect=get_db_url('telco_churn')


#this is a function that searches for local csv file that contains the telco cata and if not found it runs the queriry, caches it in your directory as a .csv file for future reference, and brings up the dataframe with telco data



def get_telco_data():
    filename = 'telco_churn.csv'
#this function quieries the codeup SQL database to to the telco_db schema and joins four tables (contract_types, customers,internet_service_types, and payment_types) and returns them all in single DataFrame titled telco_churn 
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else: telco_churn=pd.read_sql('''SELECT * FROM contract_types
    JOIN customers USING (contract_type_id)
    JOIN internet_service_types USING (internet_service_type_id)
    JOIN payment_types USING (payment_type_id)''', telco_connnect)
    telco_churn.to_csv('telco_churn.csv',index=False)
    return telco_churn