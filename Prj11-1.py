import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data into a Pandas DataFrame
data = pd.read_csv('crimeRecord1.csv')

# Data Preprocessing
# Replace missing values with 0
data.fillna(0, inplace=True)

# Define the column names for the years
years = ['Cases (2019)', 'Crime Rate (2019)', 'Cases (2020)', 'Crime Rate (2020)', 'Cases (2021)', 'Crime Rate (2021)']

# Create a figure and axis for the first plot (Crime Rates Over the Years)
plt.figure(figsize=(12, 8))

# Plot crime rates for different years
colors = ['b', 'g', 'r']
for i, year in enumerate(range(2019, 2022)):
    plt.plot(data[years[i*2+1]], data['Crime Head'], label=str(year), color=colors[i])

plt.title('Crime Rates Over the Years')
plt.ylabel('Crime Head')
plt.xlabel('Crime Rate')
plt.legend(title='Year')
plt.grid(True)

# Create a figure and axis for the second plot (Percentage Share of IPC Crimes Over the Years)
plt.figure(figsize=(8, 12))

# Visualize the percentage share of IPC crimes over the years
plt.plot(data['Percentage Share of IPC Crimes'], data['Crime Head'], marker='o', linestyle='-', color='purple')
plt.title('Percentage Share of IPC Crimes Over the Years')
plt.ylabel('Crime Head')
plt.xlabel('Percentage Share')
plt.grid(True)

# Create a figure and axis for the third plot (Top Crimes by Average Crime Rate)
plt.figure(figsize=(12, 8))

# Calculate the average crime rate for each crime head across years
average_crime_rate = data[years].mean(axis=1)

# Get the top N crimes with the highest average crime rates
top_n = 10  # Change this value to show more or fewer top crimes
top_crimes_indices = average_crime_rate.nlargest(top_n).index
top_crimes_data = data.loc[top_crimes_indices]

# Plot the top crimes
plt.barh(top_crimes_data['Crime Head'], top_crimes_data['Percentage Share of IPC Crimes'], color='skyblue')
plt.title(f'Top {top_n} Crimes by Average Crime Rate')
plt.xlabel('Percentage Share')
plt.ylabel('Crime Head')
plt.grid(axis='x', linestyle='--', alpha=0.6)

# Adjust layout for better presentation
plt.tight_layout()

# Show the plots
plt.show()
