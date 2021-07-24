import pandas as pd
import numpy as np
def preprocess():
    df = pd.read_csv('breast-cancer.csv')
    df = df.dropna(how='any',axis=1)
    df = df.drop(['id','area_worst','perimeter_se','perimeter_worst','texture_worst','radius_worst' ,'smoothness_worst' ,'compactness_worst','concavity_worst','concave points_worst','area_se','area_mean','texture_mean','perimeter_mean','radius_mean','radius_se','symmetry_worst' ,'fractal_dimension_worst','smoothness_mean' ,'compactness_mean' ,'concavity_mean' ,'concave points_mean' ,'symmetry_mean' ,'fractal_dimension_mean'],axis=1)
    df = df.dropna(how='any')
    df['target'] = np.where(df['diagnosis']== 'M', 1, 0)
    df= df.drop(['diagnosis'],axis=1)
    dataset=df.to_numpy()
    return dataset

def modus(a, n):
    max_element = max(a)
    t = max_element + 1
    count = [0] * t
    for i in range(t) :
        count[i] = 0
    for i in range(n) :
        count[a[i]] += 1
    mode = 0
    k = count[0]
    for i in range(1, t) :
        if (count[i] > k) :
            k = count[i]
            mode = i
#     print("mode = ", mode)
    return mode
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return np.sqrt(distance)
def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    val=list()
    for r in range(0,len(test_row)):
        temp=list()
#         print("data--",r,"--")
        for train_row in train:
            dist = euclidean_distance(test_row[r], train_row)
            distances.append((train_row, dist))
        distances.sort(key=lambda tup: tup[1])
        neighbors = []
        for i in range(num_neighbors):
            neighbors.append(distances[i][0])
        for i in neighbors:
            temp.append(int(i[-1]))
#         print(temp)
        val.append(modus(temp,num_neighbors))
    return val
def train_test_split(num,data):
    split=int((len(data))*num)
    X_train=data[split:]
    X_test=data[:split]

    return X_train,X_test
    

def evaluate(predict,test):
    temp_test=[]
    TP=0
    FP=0
    for i in test:
        temp_test.append(int(i[-1]))
    for i in range(len(test)):
        if predict[i]==temp_test[i]:
            TP+=1
        else:
            FP+=1
    accuracy=int((TP/(FP+TP))*100)
    print('accuracy = ',accuracy,'%')
    return accuracy
