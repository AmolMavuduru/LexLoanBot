#import numpy as np
#import pandas as pd 
#from sklearn.preprocessing import LabelEncoder
#from sklearn.externals import joblib 

def convert_to_label(term):

	if(term <= 36):
		return ' 36 months'
	else:
		return ' 60 months'


def lambda_handler(event, context):

	slots = event['currentIntent']['slots']
	State = slots['State']
	Amount = slots['Amount']
	AnnualIncome = slots['AnnualIncome']
	NumDelinq = slots['NumDelinq']
	DTI = slots['DTI']
	Term = slots['Term']
	EmpLength = slots['EmpLength']
	HomeOwn = slots['HomeOwn']
	OpenAcc = 3
	int_rate = 13.25
	Term = convert_to_label(Term)

    
   	if NumDelinq > 3 and AnnualIncome < 13000:
    	prediction = 'Not paid'
   	elif DTI > 0.8 and AnnualIncome < 14000 and EmpLength < 5:
    	prediction = 'Not paid'
    elif !HomeOwn.contains('own') and !HomeOwn.contains('Own') and EmpLength < 3:
        prediction = 'Not paid'
    elif DTI > 1.3:
        prediction = 'Not paid'
    else:
        prediction = 'Fully paid'

	if(prediction == 'Fully Paid'):

		return {
			"dialogAction": {
				"type": "Close",
				"fulfillmentState": "Fulfilled",
				"message": {
					"contentType": "PlainText",
					"content": "You will likely qualify for a loan"
				}
			}
		}
	else:

		return {
			"dialogAction": {
				"type": "Close",
				"fulfillmentState": "Fulfilled",
				"message": {
					"contentType": "PlainText",
					"content": "You will most likely not qualify for a loan"
				}
			}

		}
