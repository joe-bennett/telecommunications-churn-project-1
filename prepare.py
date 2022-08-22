#standard ds libraries
import pandas as pd
import numpy as np

# import where we can make our data splitting functions
from sklearn.model_selection import train_test_split



#the prep_telco_churn function below takes the telco_churn DataFrame and drops uneccessary columns, encodes catagorical type columns and concatenates the two. it takes this prepped DataFrame and returns it  as telco_churn


def prep_telco_churn(telco_churn):
    telco_churn = telco_churn.drop(columns=['internet_service_type_id', 'contract_type_id','payment_type_id'])

    telco_churn['gender_encoded'] = telco_churn.gender.map({'Female': 1, 'Male': 0})
    telco_churn['partner_encoded'] = telco_churn.partner.map({'Yes': 1, 'No': 0})
    telco_churn['dependents_encoded'] = telco_churn.dependents.map({'Yes': 1, 'No': 0})
    telco_churn['phone_service_encoded'] = telco_churn.phone_service.map({'Yes': 1, 'No': 0})
    telco_churn['paperless_billing_encoded'] = telco_churn.paperless_billing.map({'Yes': 1, 'No': 0})
    telco_churn['churn_encoded'] = telco_churn.churn.map({'Yes': 1, 'No': 0})
    
    dummy_df = pd.get_dummies(telco_churn[['multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type', \
                              'internet_service_type', \
                              'payment_type'
                            ]],
                              drop_first=True)
    telco_churn = pd.concat( [telco_churn, dummy_df], axis=1 )
    
    return telco_churn



#enter the name of the Dataframe and the target variable in the funcion below to split and return the data as train, validate, and test samples

def my_train_test_split(df, target):
    
    train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[target])
    train, validate = train_test_split(train, test_size=.25, random_state=123, stratify=train[target])
    
    return train, validate, test



# X_train = train.drop(columns=['survived'])
# y_train = train.survived

# X_validate = validate.drop(columns=['survived'])
# y_validate = validate.survived

# X_test = test.drop(columns=['survived'])
# y_test = test.survived