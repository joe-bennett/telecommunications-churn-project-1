


Descripton and goals:

the scope of this project can summized simply by saying I am using the available telecommunications company client data to identify factors that have statistically significant relationship to client turnover (churn) creation. For me as the data scientist my goal is to  create a classification model that more accurately than the baseline predicts churn. My next goal is to provide recommendations to reduce customer churn occurrances (increase customer retention rate) that are both meaningful yet doable. 





Questions we will use as lenses to look at and evaluate client data one at a time independently for predictors of client churn:

1) Does contract type have a significant relationship with customer churn?

2) Is there a service associated with churn more than expected?

3) Do customers who churn have a higher average monthly service cost that those who do not?

4) Does any method of payment have a positive relationship with customer churn?







Data dictionary:

Target            Datatype                Def

churn             object                  yes or no if a customer canceled services


Feature                                         Datatype                                          def

payment_type_Mailed check                       uint8                                              yes/no customer pays with mailed check
payment_type_Electronic check                   uint8                                              yes/no customer pays with e check
payment_type_Credit card (automatic)            uint8                                              yes/no customer pays with credit card
internet_service_type_Fiber optic               uint8                                              yes/no customer has fiber optic internet service
internet_service_type_None                      uint8                                              yes/no customer has no internet service 
contract_type_One year                          uint8                                              yes/no customer has a one year contract agreement
contract_type_Two year                          uint8                                              yes/no customer has a two year contract agreemnt
monthly_charges                                 float64                                            amount customer pays per month







Outline each phase of the process are distilled into six steps. they are as follows:



Planning- As with all great strategies we begin with the end in mind and work our way back from there. To do this we first concisely state our objectives ( see description above), define what success looks like, and lastly have a written "blueprint" that overlays a timeline. Our description sets forth our objectives, success is defined as delivering meaningful- yet doable mathmatically substantiated proposals/recommendations to reduce churn to my direct manager and my direct manager's manager, and this completed readme file along with written timeline will serve as blueprint to deliver at a minimum a minimally viable product by Tuesday August 23rd 1200HRS.


Acquisition- this stage is where we locate and create a path for original data source to our working enviroment. In this project all data is located in SQL database. The acquisition is achieved via creation of acquire.py file that contains the functions used to reproduce the acquisition of said data. In order garner all relevant data into our jupyter notebook enviroment basic clean-up, integration, and aggregation will need to be performed on the data in the SQL database. These steps will be addressed and repeatable with the functions inside the acquire.py file. the result will be a DataFrame in our python enviroment that contains all relevant information.



Preparation- this is the point where data tidying, cleaning, and wrangling is performed on our customer data inside our jupyter notebook enviroment. From there the data is split into three samples-  a dataframe for training the algorithms, a dataframe for validating the models developed on unseen data, a dataframe for testing the best performing model to ensure the model is able to be generalized on a final set of unseen data and not'overfitting' the training data.  A seperate file called prepare.py is where the functions to prepare our data repeatibly are stored.



Exploration- this part is where exploratoy data analyis, visualization, and feature engineering/selection is performed. Using our aforementioned questions we are asking of the data as a guide, we use statistical testing to understand variable relationships, correlations, interdependencies, etc and use visualization to convey these. Data that provides no significance in our exploration is dropped to reduce noisy data.


Modeling- Here we create a well-made generalizable model that maps relationships between our features and target outcome. Many models are evaluated on the train data set and we will take top three to evaluate on validate. While the top 3 models will be covered in the final report, only the best model will advance to move forward with the test set of data. Using the best model evaluated on the test data a .csv containing predictions in the form of 3 columns: customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn).


Delivery-  the finale is the all-encompassing delivery of the live presentation. It is here we take no more than five minutes to present the final report and convey what was performed, valuable insights learned, and conclude with actionble recommendations to reduce the customer churn moving forward. After showing the findings the floor is opened up for any follow up Q & A time.







To reproduce my work:

You should read this README.md entirely
Both the acquire.py and the prepare.py files need to be downloaded into your current working directory 
download final_report.ipynb into your current working directory
IMPORTANT you must add your own env file to your current working directory that contains host, username, and password so that you can access the codeup database
Run the final_report.ipynb








