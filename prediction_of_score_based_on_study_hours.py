# -*- coding: utf-8 -*-
"""PREDICTION OF SCORE BASED ON STUDY HOURS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ki4w_RjfQhYLNnFJT6aCL3D4zjZX29kb

# **PREDICTION OF SCORE BASED ON STUDY HOURS**

---



---

## BY : TEHSEEN MEO

---

# **Import Libraries**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""# **Data Collection**"""

url = "http://bit.ly/w-data"
data = pd.read_csv(url)
print(data)

data.head()
data.info()

"""# **Data Pre-processing**"""

X = data.iloc[:, :-1].values  # data drop last column  # input/attribute

Y = data['Scores'] #output/label

"""# **Split Dataset**"""

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 3)

"""# **ML Algorithm Training**"""

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train,Y_train)

"""# **Prediction**"""

print(X_test) #  hours in test data
Y_predict = reg.predict(X_test)
print(Y_predict) #predict score

"""# **Actual vs Predicted Score**"""

df = pd.DataFrame({'Actual': Y_test, 'Predicted': Y_predict})
df

"""# **Visualize Data**

# **Plot the linear regression graph**
"""

plt.scatter(X_train, Y_train, color='red') # Hours vs score
plt.plot(X_train, reg.predict(X_train), color='blue') # plotting the regression line
plt.title("Study Hours vs Score ")
plt.xlabel("Hours")
plt.ylabel("Score")
plt.show()

"""# **Evaluate Model**"""

from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, Y_predict))

r_squared = reg.score(X_test, Y_test)
print('R-squared:', r_squared)

"""# **Test own data**"""

hours = 9.25
Y_pred = reg.predict(np.array(hours).reshape(-1, 1))
print("No of Hours = {}".format(hours))
print("Predicted Score = {}".format(Y_pred))

# Plotting the Regression Line
plt.scatter(X_train, Y_train, color='red')  # Scatter plot of training data
plt.plot(X_train, reg.predict(X_train), color='blue')  # Regression line
plt.scatter(hours, Y_pred, color='green', marker='o')  # Predicted score point
plt.title("Study Hours vs Score")
plt.xlabel("No. Of Study Hours")
plt.ylabel("Score")
plt.show()