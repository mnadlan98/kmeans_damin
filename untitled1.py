# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f1AhgdEJUDDiFO1-iNbXXj4vaMiBSNS_
"""

import random
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import load_iris
from sklearn import tree

names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'Class']

dataset = pd.read_csv("car.data", names=names)
dataori = pd.read_csv("carori.data", names=names)

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 6].values

print(dataori)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))