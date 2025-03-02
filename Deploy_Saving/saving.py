
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
url='https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'

names=['preg','plas','pres','skin','test','mass','pedi','age','class']

df=pd.read_csv(url,names=names)
# print(df)

x=df.iloc[:,0:8]
y=df.iloc[:,8]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=101)

model=LogisticRegression()
model.fit(x_train,y_train)

accuracy=model.score(x_test,y_test)

print(accuracy)

y_pred=model.predict(x_test)

print(accuracy_score(y_test,y_pred))

# saving model
joblib.dump(model,'save_model.pkl')