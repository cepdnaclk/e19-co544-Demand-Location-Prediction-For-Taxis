import pandas as pd

# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv('merged_taxi.csv')

# Step 2: Drop the first two columns
df = df.drop(df.columns[:2], axis=1)

# Step 3: Save the modified DataFrame back to a new CSV file
df.to_csv('output.csv', index=False)
