import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Function to create a sample sales dataset and save it to 'sales_data.csv'
def create_sample_dataset(file_name):
    # Sample sales data
    data = [
        ['Date', 'Product', 'Sales'],
        ['2023-01-01', 'ProductA', 100.0],
        ['2023-01-02', 'ProductB', 150.0],
        ['2023-01-03', 'ProductA', 120.0],
        # Add more data rows as needed
    ]

    # Write the data to the CSV file
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f'Successfully created {file_name}')

# 1. Create a sample sales dataset (uncomment the line below to create the dataset)
create_sample_dataset('sales_data.csv')

# 2. Data Loading
df = pd.read_csv('sales_data.csv')  # Load the sales dataset into a Pandas DataFrame

# 3. Data Cleaning
# Check for missing values, duplicates, and perform data cleaning as needed

# 4. Exploratory Data Analysis (EDA)
# Create visualizations to understand the data better
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Sales'])
plt.title('Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.show()

# 5. Data Aggregation
total_sales = df['Sales'].sum()
avg_sales_per_day = df.groupby('Date')['Sales'].mean()

# 6. Data Filtering
filtered_data = df[df['Product'] == 'ProductA']

# 7. Statistical Analysis (using NumPy)
mean_sales = np.mean(df['Sales'])
median_sales = np.median(df['Sales'])
std_dev_sales = np.std(df['Sales'])

# 8. Additional Data Visualization
plt.hist(df['Sales'], bins=20)
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()
