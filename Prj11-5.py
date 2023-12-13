import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
data = pd.read_csv('crimeRecord1.csv')

# Step 2: Data Exploration
# Display basic information about the dataset
print(data.info())

# Step 3: Data Cleaning (if needed)
# Handle missing values, duplicates, outliers, and data type issues as necessary

# Step 4: Data Visualization
# Example: Create a bar chart of 'Cases (2019)' by 'Crime Head'
plt.figure(figsize=(12, 6))
sns.barplot(x='Cases (2019)', y='Crime Head', data=data, palette='viridis')
plt.title('Cases in 2019 by Crime Head')
plt.xlabel('Cases (2019)')
plt.ylabel('Crime Head')
plt.xticks(rotation=90)
plt.show()

# Example: Create a scatter plot of 'Crime Rate (2019)' vs 'Cases (2019)'
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Crime Rate (2019)', y='Cases (2019)', data=data, hue='Crime Head', palette='Set1')
plt.title('Crime Rate vs Cases in 2019')
plt.xlabel('Crime Rate (2019)')
plt.ylabel('Cases (2019)')
plt.show()

# Step 5: Data Analysis (you can perform statistical analysis here)

# Step 6: Data Visualization (continued)
# Exclude non-numeric columns and create a correlation heatmap
numeric_columns = data.select_dtypes(include=[np.number])
correlation_matrix = numeric_columns.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Step 7: Further analysis and visualizations as needed

# Step 8: Conclusion and Reporting
# Summarize findings and insights from the data analysis

# Optionally, you can save the visualizations as image files
# plt.savefig('visualization.png')

# Optionally, you can export the cleaned dataset to a new CSV file
# data.to_csv('cleaned_data.csv', index=False)
