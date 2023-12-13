# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv('crimeRecord1.csv')

# Explore the dataset
print(df.head())

# Visualize the dataset
sns.pairplot(df)

# Define the features and the target
X = df[['Cases (2019)', 'Cases (2020)', 'Cases (2021)']].values
y = df['Percentage Share of IPC Crimes'].values

# Compute the mean of the features and the target
X_mean = np.mean(X, axis=0)
y_mean = np.mean(y)

# Compute the terms needed for the numator and denominator of beta
numerator = 0
denominator = 0
for i in range(len(X)):
    numerator += (X[i] - X_mean) * (y[i] - y_mean)
    denominator += (X[i] - X_mean) ** 2

# Compute beta and alpha
beta = numerator / denominator
alpha = y_mean - np.dot(beta, X_mean)

print(f"The linear model is: Y = {alpha} + {beta[0]}*X1 + {beta[1]}*X2 + {beta[2]}*X3")

# Plotting Values and Regression Line
max_x = np.max(X) + 100
min_x = np.min(X) - 100

# Calculating line values x and y
x = np.linspace(min_x, max_x, 1000)
Y = alpha + beta[0] * x + beta[1] * x + beta[2] * x

# Ploting Line
plt.plot(x, Y, color='#58b970', label='Regression Line')
# Ploting Scatter Points
plt.scatter(X[:,0], y, c='#ef5423', label='Scatter Plot')

plt.xlabel('Cases (2019)')
plt.ylabel('Percentage Share of IPC Crimes')
plt.legend()
plt.show()
