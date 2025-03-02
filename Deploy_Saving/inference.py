import joblib

model=joblib.load('save_model.pkl')

res=model.predict([[1,1,1,1,1,1,1,1]])

print(res)