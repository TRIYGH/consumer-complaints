#W3D2   -   complaint

import numpy as np
import pandas as pd
from pandas import DataFrame, Series
from datetime import datetime


def load_file():
    column_names = ['Complaint ID','Product','Sub-product','Issue','Sub-issue','State','ZIP code','Submitted via','Date received','Date sent to company','Company','Company response','Timely response?','Consumer disputed?']
    return pd.read_csv('complaints_dec_2014.csv')



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

entire_cons_compl.index = pd.to_datetime(complaint_dates)#, format='%m/%d/%Y')

entire_cons_compl['Weekday'] = entire_cons_compl.index.weekday

entire_cons_compl.head()
# DOC_list = complaint_dates.weekday
INDEX = complaint_dates.value_counts().index
print(INDEX)
input()
VAL = complaint_dates.value_counts()
# now2 = datetime.datetime.now("12-31-1988")
day = datetime.strptime('12-31-1988', '%m-%d-%Y')
# day = (complaint_dates.value_counts().index)[0].now
print(day.weekday())
input()

iday = complaint_dates.value_counts().index[0]
day = datetime.strptime(iday, '%m/%d/%Y')
print(day)
print(day.strftime("%A"))
input()


for each in INDEX:
    print(each)
input()

x=complaint_dates.value_counts()
y=entire_cons_compl['Weekday'].value_counts()
a=(entire_cons_compl['Weekday'].value_counts())[0]
b=(entire_cons_compl['Weekday'].value_counts())[1]
print(y.index, y)
input()
print(y,"YYYYY",a,b)
count = 0
days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'SUnday']
for each in y:
    print(days[count],each)
    count+=1
input()
print(y)
# for each in x:
#     print(each, entire_cons_compl['Weekday'])
print(y[1])
