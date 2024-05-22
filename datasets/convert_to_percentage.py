#change 1000 to 100 for percentages
#run the script in the same folder as the output_file.csv
#output will be a new csv file with the percentages named output_percentage_values.csv
#percentage means the percentage of traffic of a region when compared with the other regions for a particular day

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('output_file.csv')

# Function to replace each element in the row with the percentage of the row's total
def row_to_percentage(row):
    total = row.sum()
    return ((row / total) * 1000) if total != 0 else row

# Apply the function to each row except the first and to all columns except the first column
df.iloc[:, 1:] = df.iloc[:, 1:].apply(row_to_percentage, axis=1)

# Save the modified DataFrame back to a CSV file
df.to_csv('output_percentage_values.csv', index=False)
