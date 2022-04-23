import numpy as np
import pandas as pd
import keras
import tensorflow as tf
import matplotlib.pyplot as plt
from matplotlib import style
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing, svm, metrics  
import math
from keras import metrics
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

train_v = 'train_values.csv'
train_l = 'train_labels.csv'
df_tval = pd.read_csv(train_v, index_col=0)
#df_tval
df_tlab = pd.read_csv(train_l, index_col=0)
#df_tlab

selected_features = [ ]

t_val_subset = df_tval[selected_features]

#replace the strings in thal column with corresponding numbers
df_tval = df_tval.replace({'normal': 2, 'reversible_defect': 1, 'fixed_defect': 0})
X = np.array(df_tval)
X = preprocessing.scale(X)
y = np.array(df_tlab)

X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.20, random_state=13)
#def random_forest_classifier(features, target):
   #clf = RandomForestClassifier()
    #clf.fit(features, target)
   # return clf
clf = RandomForestRegressor(n_estimators = 3000, random_state = 10)
# Train the model on training data
clf.fit(X_train, y_train)

# Use the forest's predict method on the test data
prediction_s = clf.predict(X_test)
# Calculate the absolute errors
errors_s = abs(prediction_s - y_test)

# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors_s - y_test)
# Calculate accuracy
accuracy = 100 - np.mean(mape)

sklearn.metrics.log_loss(y_test, prediction_s, normalize=True, sample_weight=None, labels=None)
accuracy = clf.score(X_test, y_test) #test Accuracy squared error for linreg

path = 'test_values.csv'

df_path = pd.read_csv(path, index_col = 0)
df_path = df_path.replace({'normal': 2, 'reversible_defect': 1, 'fixed_defect': 0})
test_val = np.array(df_path)
test_val = preprocessing.scale(test_val)
test_predictions = clf.predict(test_val)
test_predictions

save_file = pd.DataFrame(test_predictions, columns=['food_to_cook'])
save_file.index.names = ['weight_id']
#test_predictions
file = pd.read_csv( 'submission_format.csv')
file= file.drop(columns = ['food_to_cook'])
save_file = pd.DataFrame(test_predictions, columns=['food_to_cook'])
#result = pd.merge(file, save_file, left_index=True, right_index=True, how='right');
results = pd.concat([file, save_file], axis=1)
results = results.set_index(keys='total_weight')
results
