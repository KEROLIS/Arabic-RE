
import pandas as pd
import os 
import re

dir_path = os.path.dirname(os.path.realpath('__file__'))
print(dir_path)

data=pd.read_csv(dir_path+"/regular_ex_Ar.csv")

def cleaning (data) :
    w=[]
    for s in data :
        s= re.sub(r'[^\w\s]','',s)
        s= re.sub(r'[a-z]','',s)
        s= re.sub(r'[A-Z]','',s)
        s= re.sub(r'[0-9]','',s)
        s= re.sub(r'_',' ',s)
    
        s= re.sub(r'أ','ا',s)
        s=re.sub(r'ؤ','و',s)
        s= re.sub(r'ة','ه',s)
        s= re.sub(r'إ','ا',s)
        w.append(s)
    return w

print ("data before cleaning :")
print(data['text'])

data['text']=cleaning(data['text'])

print ("data after cleaning :")
print (data['text'])

data.to_csv(dir_path+'/data_after_cleaning.csv')
