# -*- coding: utf-8 -*-
## Mariah Harvey
## August 5, 2016
## API call for Census Demography

from requests import *
import unicodecsv as csv
import pandas as pd
import itertools
import json as simplejson

# Setup API components
# Example input http://api.census.gov/data/2013/acs5?get=NAME,B01001_001E&for=county:195&in=state:02&key=
base_url='http://api.census.gov/data/2014/acs5?get=NAME,'
api_county='&for=county:'
api_state='&in=state:'
api_key='&key=6109c5b9cff812221a07c30c3f28b66cdd1347a3'
value=[]

##create list of possible ends 

end=[]
for i in range(1, 50):
    a=str(i).zfill(3)
    end.append(a)
B_list=['B01001_']
t='E'
x=','


list1=[]
for s in B_list:    
    for i in end:
        name=s+i+t
        list1.append(name)


# Call API
def call_API(county, state):
    for l in list1:
        url=base_url+l+api_county+county+api_state+state+api_key
        response=get(url)
        data=response.json()
        len_data=len(data)
        names=data[0]
        data=data[1:len_data]
        value.append(pd.DataFrame(data,columns=names))

    alpha=value[0]
    alpha=alpha[['NAME','state','county']]

    for i in value:
        alpha=pd.merge(alpha,i,on=('NAME', 'county','state'), how='left')

    return alpha

