import matplotlib.pyplot as plt
# Input Data
print("Fill in the details")
try:
    No_of_labels = int(input("Number of labels: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

def categories():
    categories =[]
    print("Enter Data in categories:")
    for x in range(No_of_labels):
        data = input("Enter: ")
        categories.append(data)
    return categories

def values():
    values = []
    print("Enter data in values:")
    for x in range(No_of_labels):
        data = input("Enter: ")
        values.append(data)
    return values

# Sample data
# categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
# values = [10, 24, 16, 30]

# Create a bar chart
plt.bar(categories(), values())

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')

# Show the chart
plt.show()
