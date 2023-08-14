import pandas as pd
import math
import numpy as np

def entropy_dataset(target):
    count={}
    n=float(len(target))
    val=0.0
    for i in range(len(target)):
        if target[i] not in count.keys():
            count[target[i]]=1
        else:
            count[target[i]]+=1
    for i in list(count.values()):
        val+=(-(float(i)/float(n))*(math.log2(float(i)/float(n))))
    val=round(val,3)
    return val

def entropy_col(col,target,i):
    entropy=0.0
    result_dict = {}
    print("\n**********",i,"**********\n")
    for i in range(len(col)):
        col_name = col[i]
        activity = target[i]
        if col_name in result_dict:
            result_dict[col_name][activity] = result_dict[col_name].get(activity, 0) + 1
        else:
            result_dict[col_name] = {activity: 1}
    for i in result_dict.keys():
        sum=0.0
        val1=0.0
        for j in result_dict[i].keys():
            sum+=result_dict[i][j]
        for j in result_dict[i].keys():
            value=float(result_dict[i][j])
            val1+=(-(value/sum)*(math.log2(value/sum)))
            val1=round(val1,3)
        print("Entropy of",i,"=",val1)
        entropy+=((sum/len(target))*val1)
    entropy=round(entropy,3)
    print()
    print(result_dict)
    return entropy

filename=input("Enter filename:")
data=pd.read_csv(filename)
target_col=input("Enter target column name:")
ent_data=entropy_dataset(data[target_col])
column_names = data.columns.tolist()
info_col={}
for i in column_names[:len(column_names)-1]:
    ent_col=entropy_col(list(data[i]),data[target_col],i)
    print()
    print("Entropy of Dataset =",ent_data)
    print("Entropy of",i,"=",ent_col)
    if i not in info_col.keys():
      info_col[i]=round(ent_data-ent_col,3)
    print("Information gain of",i,"=",ent_data,"-",ent_col,"=",info_col[i])
print("\n****************************\n")
for i in column_names[:len(column_names)-1]:
    print("Information Gain of",i,"=",info_col[i])
max_key = max(info_col, key=info_col.get)
print("\n****************************\n")
print("Root node:", max_key,"with information gain =",info_col[max_key])
print("\n****************************\n")