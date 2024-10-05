#Importing libraries
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset = pd.read_csv('DataScience/Salary.csv')
dataset
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


#Spliting this dataset into training and learning
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3,random_state = 0)