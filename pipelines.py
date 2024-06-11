# import dependencies
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC


# change data with label encoder
def label(y_train,y_test):
    le = LabelEncoder()

    y_train_le = le.fit_transform(y_train)
    y_test_le = le.transform(y_test)
    print(f'train:{y_train_le}\ntest:{y_test_le}')
    return y_train_le, y_test_le


#scale data with standardscaler
def scaled(x):
    scaled = StandardScaler()
    scaled.fit(x)
    X_train_scaled = scaled.transform(x)
    X_train_scaled
    return X_train_scaled














def logistic(x_train_scaled,y_train_le):
    lr = LogisticRegression(random_state=1,max_iter=120)
    lr.fit(x_train_scaled,y_train_le)
    print(f'training:{lr.score(x_train_scaled,y_train_le)}\ntesting{lr.score(x_test_scaled,y_test_le)}')
    return x,y

def svc_poly(x,y):
    svc = SVC(kernel='poly')
    svc.fit(x,y)
    print(f'training:{svc.score(x,y)}\ntesting:{svc.score(x,y)}')