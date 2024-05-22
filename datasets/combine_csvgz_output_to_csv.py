#create a folder in the current directory named total_csv_folder
#add all the csv, csv.gz files inside
#run the python script in the current folder
#will output a single csv combining all named output_file.csv in the current folder


import pandas as pd
import gzip
import os

def combine_csv_files(input_directory, output_file):
    # List to hold individual dataframes
    dataframes = []

    # Iterate over all files in the input directory
    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)
        
        # Process .csv.gz files
        if filename.endswith(".csv.gz"):
            with gzip.open(file_path, 'rt') as f:
                df = pd.read_csv(f)
                dataframes.append(df)
        
        # Process .csv files
        elif filename.endswith(".csv"):
            df = pd.read_csv(file_path)
            dataframes.append(df)
    
    # Concatenate all dataframes
    combined_df = pd.concat(dataframes, ignore_index=True)
    
    # Write the combined dataframe to a .csv file
    combined_df.to_csv(output_file, index=False)

# Usage
input_directory = 'total_csv_folder'
output_file = 'output_file.csv'
combine_csv_files(input_directory, output_file)