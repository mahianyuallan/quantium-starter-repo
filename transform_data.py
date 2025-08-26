import pandas as pd
import glob

# Path to your data folder (adjust if needed)
data_path = "data/*.csv"

# Get list of all CSVs in the data folder
csv_files = glob.glob(data_path)

# Create an empty list to hold dataframes
dfs = []

for file in csv_files:
    # Read each CSV
    df = pd.read_csv(file)
    
    # Filter only pink morsels
    df = df[df["product"] == "pink morsel"]
    
    # Calculate sales
    df["sales"] = df["quantity"] * df["price"]
    
    # Keep only required columns
    df = df[["sales", "date", "region"]]
    
    dfs.append(df)

# Concatenate all into one dataframe
final_df = pd.concat(dfs, ignore_index=True)

# Save to CSV
final_df.to_csv("formatted_sales.csv", index=False)

print("✅ formatted_sales.csv created successfully!")
