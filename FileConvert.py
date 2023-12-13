import pandas as pd

# Specify the path to your Excel file (replace 'input.xlsx' with your file)
excel_file = 'input.xlsx'

# Specify the path where you want to save the CSV file (replace 'output.csv' with your desired file name)
csv_file = 'output.csv'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file)

# Save the DataFrame to a CSV file
df.to_csv(csv_file, index=False)

print(f'File "{excel_file}" converted to "{csv_file}" successfully.')
