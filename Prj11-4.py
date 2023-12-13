import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Data Collection
data = pd.read_csv('crimeRecord1.csv')

# Step 2: Data Preprocessing
# Handle missing values, duplicate rows, and outliers
data.drop_duplicates(inplace=True)
data.dropna(inplace=True)

# Step 3: Exploratory Data Analysis (EDA)
# Visualize the data to gain insights
# Example: Histogram and Pair Plot
plt.figure(figsize=(8, 6))
sns.histplot(data['Cases (2019)'], bins=20, kde=True)
plt.show()

sns.pairplot(data[['Cases (2019)', 'Cases (2020)', 'Cases (2021)']])
plt.show()

# Step 4: Feature Engineering
# Create new features if needed using NumPy and Pandas
# Encode categorical variables using Pandas
data = pd.get_dummies(data, columns=['Crime Head'], drop_first=True)

# Step 5: Train-Test Split
def train_test_split_custom(data, test_size=0.2):
    np.random.seed(42)
    mask = np.random.rand(len(data)) < (1 - test_size)
    train_data = data[mask]
    test_data = data[~mask]
    return train_data, test_data

train_data, test_data = train_test_split_custom(data)

# Step 6: Implement Logistic Regression (Custom Implementation)
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def initialize_parameters(dim):
    return np.zeros(dim)

def cost_function(y, y_pred):
    m = len(y)
    return -(1/m) * np.sum(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))

def gradient_descent(X, y, parameters, learning_rate, num_iterations):
    m = len(y)
    costs = []
    for _ in range(num_iterations):
        z = np.dot(X, parameters)
        y_pred = sigmoid(z)
        gradient = np.dot(X.T, (y_pred - y)) / m
        parameters -= learning_rate * gradient
        cost = cost_function(y, y_pred)
        costs.append(cost)
    return parameters, costs

# Prepare the data
X_train = train_data.drop('Percentage Share of IPC Crimes', axis=1).values
y_train = train_data['Percentage Share of IPC Crimes'].values.reshape(-1, 1)
X_test = test_data.drop('Percentage Share of IPC Crimes', axis=1).values
y_test = test_data['Percentage Share of IPC Crimes'].values.reshape(-1, 1)

# Initialize parameters and perform gradient descent
initial_parameters = initialize_parameters(X_train.shape[1])
learning_rate = 0.01
num_iterations = 1000
final_parameters, costs = gradient_descent(X_train, y_train, initial_parameters, learning_rate, num_iterations)

# Step 7: Model Evaluation (Custom Implementation)
def predict(X, parameters):
    z = np.dot(X, parameters)
    y_pred = sigmoid(z)
    return (y_pred >= 0.5).astype(int)

# Predict on the test set
y_pred = predict(X_test, final_parameters)

# Calculate accuracy
accuracy = np.mean(y_pred == y_test)
print(f"Accuracy: {accuracy:.2f}")

# Step 8: Visualization and Reporting
# Create visualizations using Matplotlib and Seaborn
plt.figure(figsize=(8, 6))
# Your visualization code here
plt.show()

# Step 9: Documentation and Reporting
# Document your code and findings in a Jupyter Notebook or report.
