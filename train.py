
#Importing libraries  and Loading the dataset
import pandas as pd

drug_df=pd.read_csv('Data\drug200.csv')
drud_df=drug_df.sample(frac=1)
drug_df.head(3)

from sklearn.model_selection import train_test_split
x=drug_df.drop('Drug',axis=1)
y=drug_df['Drug']

print(x.shape,y.shape)

"""Train Test Split"""

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=125)

print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)

"""Machine Learning Pipeline"""

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler

cat_col=[1,2,3]
num_col=[0,4]

transform=ColumnTransformer(
    [
        ('encoder',OrdinalEncoder(),cat_col),
        ('num_imputer',SimpleImputer(strategy='median'),num_col),
        ('num_scaler',StandardScaler(),num_col)
    ]
)

pipe=Pipeline(
    steps=[
        ('preprocessing',transform),
        ('model',RandomForestClassifier(n_estimators=100,random_state=150))
    ]
)

pipe.fit(x_train,y_train)

"""Model Evaluation"""

from sklearn.metrics import classification_report
y_pred=pipe.predict(x_test)
report=classification_report(y_test,y_pred)

print(report)

with open('Result\metrics.txt','w') as outfile:
    outfile.write(f'\nclassification_report = {report}')

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay,confusion_matrix
cm=confusion_matrix(y_test,y_pred,labels=pipe.classes_)
disp=ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=pipe.classes_)
disp.plot()
plt.savefig('Result\model_results.png',dpi=120)

"""Saving the Model"""

import skops.io as sio

sio.dump(pipe,'Model\drug_pipeline.skops')

from skops import io as sio

file_path = 'Model\drug_pipeline.skops'

# Open the file in binary mode
with open(file_path, "rb") as f:
    untrusted = sio.get_untrusted_types(file=f)


print(untrusted)

import numpy as np

trusted = ['np.dtype']

with open(file_path,'rb') as f:
    model = sio.load(file=f, trusted=untrusted)

print(model)

