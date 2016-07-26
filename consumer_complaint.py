#W3D2   -   complaint

import numpy as np
import pandas as pd
from pandas import DataFrame, Series


def load_file():
    column_names = ['Complaint ID','Product','Sub-product','Issue','Sub-issue','State','ZIP code','Submitted via','Date received','Date sent to company','Company','Company response','Timely response?','Consumer disputed?']
    return pd.read_csv('complaints_dec_2014.csv', names=column_names)



entire_cons_compl = load_file()
# print(cons_compl)

#------------------------------------------------------

prodID_index = entire_cons_compl.pop('Product')
entire_cons_compl.set_index(prodID_index)

# print(prodID_index)
# for each in prodID_index:
#     print(each,end='   ')
# input()

num_complaints_by_prod = prodID_index.value_counts()
print(num_complaints_by_prod)
input()
#------------------------------------------------------
comp_index = entire_cons_compl.pop('Company')
num_complaints_by_company = comp_index.value_counts()
# print(num_complaints_by_company.shape)
# input()
# for i in range(10):
#     print(i,num_complaints_by_company[i])
#
print(num_complaints_by_company)
# input()
# x=0
# for each in num_complaints_by_company:
#     print(each, num_complaints_by_company[x])
#     x+=1
#     if x > 10:
#         input()
#         break
#------------------------------------------------------

response_index = entire_cons_compl.pop('Company response')
num_complaints_by_response = response_index.value_counts()

print(num_complaints_by_response)
input()
#------------------------------------------------------

complaint_dates = entire_cons_compl.pop('Date received')
for each in complaint_dates:
    print(len(each))
    input()
print(complaint_dates)
input()

# day_of_complaint = pd.to_datetime(complaint_dates, format='%m/%d/%Y', infer_datetime_format=True)
#
# DOC_list = complaint_dates.weekday
# print(day_of_complaint, DOC_list)
