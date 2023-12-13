# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Stage 1: Data Collection and Preparation
# Load the dataset
crime_data = pd.read_csv('laRecord.csv')

# Clean and preprocess the data
# Handle missing values, outliers, and data inconsistencies
crime_data.dropna(inplace=True)
crime_data = crime_data[crime_data['Rate of Cognizable Crimes (IPC) (2021)'] > 0]

# Stage 2: Exploratory Data Analysis
# Basic statistics
summary_stats = crime_data.describe()

# Visualize data distributions
plt.figure(figsize=(12, 6))
plt.hist(crime_data['Rate of Cognizable Crimes (IPC) (2021)'], bins=30, color='b', alpha=0.7)
plt.title('Crime Rates in 2021')
plt.xlabel('State/UT')
plt.ylabel('Crime Rate')
plt.show()

# Select only numeric columns for correlation calculation
numeric_columns = ['Mid-Year Projected Population (in Lakhs) (2021)', 'Rate of Cognizable Crimes (IPC) (2021)', 'Chargesheeting Rate (2021)']
numeric_data = crime_data[numeric_columns]

# Calculate the correlation matrix
correlation_matrix = numeric_data.corr()

# Rest of your code for plotting the correlation matrix
plt.figure(figsize=(10, 6))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest', aspect='auto')
plt.colorbar()
plt.title('Correlation Matrix')
plt.xticks(range(len(correlation_matrix)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix)), correlation_matrix.columns)
plt.show()


# Stage 3: Customer Segmentation (NumPy only, without scipy)
# Select features for segmentation
features = ['Mid-Year Projected Population (in Lakhs) (2021)', 'Chargesheeting Rate (2021)']

# Standardize the data using NumPy
scaled_data = (crime_data[features] - crime_data[features].mean()) / crime_data[features].std()

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
plt.figure(figsize=(8, 4))
plt.plot(K_range, distortions, marker='o', linestyle='-', color='b')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Distortion')
plt.xticks(K_range)
plt.show()

# Based on the Elbow method, select an appropriate value for K (number of clusters)

# Perform K-means clustering using NumPy
k = 3  # Choose an appropriate K
centroids = scaled_data.sample(n=k).to_numpy()
distances = np.linalg.norm(scaled_data[:, np.newaxis, :] - centroids, axis=2)
clusters = np.argmin(distances, axis=1)
crime_data['cluster'] = clusters

# Stage 4: Sales Analysis (Matplotlib only)
# You can add additional analysis or visualizations using the new dataset here.

# Stage 5: Recommender System (Optional)

# Stage 6: Actionable Insights
# Summarize key findings and recommendations based on customer segmentation and analysis.

