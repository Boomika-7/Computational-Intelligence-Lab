import pandas as pd
import random
from sklearn.metrics import confusion_matrix
random.seed(0)

def euclidean_distance(x1, x2):
    distance = 0
    for i in range(len(x1)):
        distance += (float(x1[i]) - float(x2[i])) ** 2
    return distance ** 0.5

def knn_classifier(X_train, y_train, test_ins, k):
    distances = [euclidean_distance(test_ins, x_train) for x_train in X_train]
    df=pd.DataFrame({"Distance":distances,"Label":y_train})
    df['Rank'] = df['Distance'].rank()
    print("\nDISTANCE BETWEEN TEST INSTANCE AND ALL TRAIN DATA\n")
    print(df)
    print()
    top_k=df.nsmallest(k, 'Rank')
    print("K-NEAREST NEIGHBORS\n")
    print(top_k)
    print("\nMAJORITY VOTE\n")
    votes = top_k['Label'].value_counts().reset_index()
    votes.columns = ['Label', 'Vote']
    print(votes)
    y_pred=votes.loc[votes['Vote'].idxmax(), 'Label']
    return y_pred

#PRE-PROCESSING
filename=input("Enter filename:")
data=pd.read_csv(filename)
data['gender'] = data['gender'].map({'Male': 1, 'Female': 2,'Other':0})
data['smoking_history'] = data['smoking_history'].map({'No Info': 5, 'never': 4,'former':3,'current':2,'not current':1,'ever':0})

#SAMPLING
df_1=data[data["diabetes"] == 1]
df_0=data[data["diabetes"] == 0]
df_11=df_1[:50]
df_00=df_0[:50]
data=pd.concat([df_11,df_00])

#TRAIN-TEST SPLIT
print("\nDataset has",len(data),"rows")
data = data.sample(frac = 1,random_state=42)
train_size = int(len(data) * 0.8)
test_size = len(data) - train_size
print("Train Size:",train_size)
print("Test Size:",test_size)
target=data["diabetes"]
data=data.drop("diabetes",axis=1)

X_train = data.iloc[:train_size]
X_test = data.iloc[train_size:]
Y_train=target[:train_size]
Y_test=target[train_size:]
print("\nTRAIN SET\n")
print(X_train)

Y_train = Y_train.values.tolist()
Y_test = Y_test.values.tolist()
X_train = X_train.values.tolist()
X_test = X_test.values.tolist()

#TEST INSTANCE
print("\nEnter test instance:")
data_test_instance=[]
for i in range(8):
    val=float(input())
    data_test_instance.append(val)
print()
print("TEST INSTANCE DATA: ",data_test_instance)

#MODEL BUILDING
print()
k=int(input("Enter value of k(neighbors):"))
y_pred = knn_classifier(X_train, Y_train, data_test_instance, k)

#MANUAL TESTING1
print("\nPredicted label:",y_pred)