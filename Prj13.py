import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import datetime

# Function to create a sample dataset and save it to 'ecommerce_data.csv'
def create_sample_dataset(file_name):
    # Generate sample data using NumPy's random functions
    np.random.seed(0)  # Set a seed for reproducibility
    n_samples = 100

    customer_ids = np.arange(1, n_samples + 1)
    customer_names = np.array([f"Customer_{i}" for i in customer_ids])
    emails = np.array([f"customer{i}@example.com" for i in customer_ids])
    transaction_ids = np.arange(1, n_samples + 1)
    purchase_dates = np.array([datetime.date(2023, np.random.randint(1, 13), np.random.randint(1, 29)) for _ in range(n_samples)])
    total_amounts = np.round(np.random.uniform(10, 200, n_samples), 2)
    product_ids = np.random.randint(1, 21, n_samples)
    product_names = np.array([f"Product_{i}" for i in product_ids])
    prices = np.round(np.random.uniform(5, 50, n_samples), 2)

    data = list(zip(customer_ids, customer_names, emails, transaction_ids, purchase_dates, total_amounts, product_ids, product_names, prices))

    # Write the data to the CSV file
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['customer_id', 'customer_name', 'email', 'transaction_id', 'purchase_date', 'total_amount', 'product_id', 'product_name', 'price'])
        writer.writerows(data)

    print(f'Successfully created {file_name}')

# Create the 'ecommerce_data.csv' file using NumPy random data generation
create_sample_dataset('ecommerce_data.csv')

# Load the data into a pandas DataFrame
df = pd.read_csv('ecommerce_data.csv')

# Data Analysis and Visualization

# Sample data analysis: Calculate total revenue
total_revenue = df['total_amount'].sum()

# Sample data analysis: Get average order value
average_order_value = df.groupby('transaction_id')['total_amount'].sum().mean()

# Sample data analysis: List top-selling products
top_selling_products = df['product_name'].value_counts().head(5)

# Data Visualization with Matplotlib

# Create a bar chart for top-selling products
plt.figure(figsize=(10, 6))
top_selling_products.plot(kind='bar', color='skyblue')
plt.title('Top Selling Products')
plt.xlabel('Product Name')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the bar chart as a PNG image
plt.savefig('top_selling_products.png')

# Show the bar chart
plt.show()

# Print analysis results
print("Total Revenue:", total_revenue)
print("Average Order Value:", average_order_value)
print("Top Selling Products:")
print(top_selling_products)
