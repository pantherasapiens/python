import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv("laRecord.csv")

# Extract relevant columns
years = ['2019', '2020', '2021']
population = 'Mid-Year Projected Population (in Lakhs) (2021)'
crime_rate = 'Rate of Cognizable Crimes (IPC) (2021)'
chargesheet_rate = 'Chargesheeting Rate (2021)'

# Define colors for bars
colors_red = plt.cm.Reds  # Shades of red colormap
colors_green = plt.cm.Greens  # Shades of green colormap

# Analyze and plot data for each year
for year in years:
    # Plot the crime rate for each state/UT as a bar chart in shades of red
    plt.figure(figsize=(12, 6))
    plt.bar(data['State/UT'], data[crime_rate], color=colors_red(data[crime_rate] / max(data[crime_rate])))
    plt.xlabel('State/UT')
    plt.ylabel('Crime Rate')
    plt.title(f'Crime Rate in {year}')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(f'crime_rate_{year}.png')  # Save the graph
    plt.show()

    # Create a bar chart for chargesheet rate in shades of green
    plt.figure(figsize=(12, 6))
    plt.bar(data['State/UT'], data[chargesheet_rate], color=colors_green(data[chargesheet_rate] / max(data[chargesheet_rate])))
    plt.xlabel('State/UT')
    plt.ylabel('Chargesheet Rate')
    plt.title(f'Chargesheet Rate in {year}')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(f'chargesheet_rate_{year}.png')  # Save the graph
    plt.show()

# Calculate and plot statistics for all years combined
plt.figure(figsize=(12, 6))
x = range(len(data['State/UT']))
plt.plot(x, data[crime_rate], label='Crime Rate', marker='o', color='red')
plt.plot(x, data[chargesheet_rate], label='Chargesheet Rate', marker='o', color='green')
plt.xlabel('State/UT (Index)')
plt.ylabel('Rate')
plt.title('Crime Rate vs. Chargesheet Rate Over Years')
plt.xticks(x, data['State/UT'], rotation=90)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the last graph to a file (e.g., PNG)
plt.savefig('crime_vs_chargesheet.png')

# Show the plot (optional)
plt.show()
