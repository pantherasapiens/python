# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Stage 1: Data Collection and Preparation
# Load the dataset(s)
sales_data = pd.read_csv('Book2.csv')
customer_data = pd.read_csv('Book3.csv')
product_data = pd.read_csv('Book4.csv')

# Merge relevant datasets
merged_data = pd.merge(sales_data, customer_data, on='Crime Rate', how='left')
merged_data = pd.merge(merged_data, product_data, on='Crime Head', how='left')

# Clean and preprocess the data
# Handle missing values, outliers, and data inconsistencies
merged_data.dropna(inplace=True)
merged_data = merged_data[merged_data['quantity'] > 0]

# Stage 2: Exploratory Data Analysis
# Basic statistics
summary_stats = merged_data.describe()

# Visualize data distributions
plt.figure(figsize=(12, 6))
plt.hist(merged_data['Percentage Share of IPC Crimes'], bins=30, color='b', alpha=0.7)
plt.title('2019')
plt.xlabel('Crime Head')
plt.ylabel('Crime Rate')
plt.show()

# Correlation matrix
correlation_matrix = merged_data.corr()
plt.figure(figsize=(10, 6))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest', aspect='auto')
plt.colorbar()
plt.title('Correlation Matrix')
plt.xticks(range(len(correlation_matrix)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix)), correlation_matrix.columns)
plt.show()

# Stage 3: Customer Segmentation (NumPy only, without scipy)
# Select features for segmentation
features = ['frequency', 'recency', 'monetary']

# Standardize the data using NumPy
scaled_data = (merged_data[features] - merged_data[features].mean()) / merged_data[features].std()

# Determine the optimal number of clusters (K) using the Elbow method (NumPy implementation)
distortions = []
K_range = range(1, 11)
for k in K_range:
    centroids = scaled_data.sample(n=k).to_numpy()
    distances = np.linalg.norm(scaled_data[:, np.newaxis, :] - centroids, axis=2)
    min_distances = np.min(distances, axis=1)
    distortion = np.sum(min_distances**2) / scaled_data.shape[0]
    distortions.append(distortion)

# Plot the Elbow method to choose K
# plt.figure(figsize=(8, 4))
# plt.plot(K_range, distortions, marker='o', linestyle='-', color='b')
# plt.title('Elbow Method for Optimal K')
# plt.xlabel('Number of Clusters (K)')
# plt.ylabel('Distortion')
# plt.xticks(K_range)
# plt.show()

# Based on the Elbow method, select an appropriate value for K (number of clusters)

# Perform K-means clustering using NumPy
k = 3  # Choose an appropriate K
centroids = scaled_data.sample(n=k).to_numpy()
distances = np.linalg.norm(scaled_data[:, np.newaxis, :] - centroids, axis=2)
clusters = np.argmin(distances, axis=1)
merged_data['cluster'] = clusters

# Stage 4: Sales Analysis (Matplotlib only)
# Calculate total revenue
merged_data['total_revenue'] = merged_data['quantity'] * merged_data['purchase_amount']

# Aggregate sales data by month
monthly_sales = merged_data.groupby(pd.to_datetime(merged_data['purchase_date']).dt.to_period('M'))['total_revenue'].sum()

# Plot monthly sales
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', linestyle='-', color='g')
plt.title('Percentage Share of IPC Crimes')
plt.xlabel('Crime Head')
plt.ylabel('Crime Rate')
plt.xticks(rotation=45)
plt.show()

# Additional analysis and visualization can be added here as needed.

# Stage 5: Recommender System (Optional)

# Stage 6: Actionable Insights
# Summarize key findings and recommendations based on customer segmentation and sales analysis.
