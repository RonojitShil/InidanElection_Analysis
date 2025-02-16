import pandas as pd
import numpy as np
# Load the dirty dataset
file_path = "indian_election_dataset.csv"
df = pd.read_csv(file_path)
# 1. Handling NULL Values
print("Missing values before:")
print(df.isnull().sum())
df.fillna({'pc_type': 'Unknown', 'cand_sex': 'Unknown'}, inplace=True)
df.dropna(inplace=True)  # Dropping remaining rows with NULLs
print("Missing values after:")
print(df.isnull().sum())
# 2. Removing Duplicates
print("Duplicates before:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("Duplicates after:", df.duplicated().sum())
# 3. Standardizing Data Formats
df['partyname'] = df['partyname'].str.replace("_", " ").str.title()
df['pc_name'] = df['pc_name'].str.title()
df['st_name'] = df['st_name'].str.title()
# 4. Correcting Inconsistent Data
df['cand_sex'] = df['cand_sex'].replace({
    'M': 'Male', 'MALE': 'Male', 'F': 'Female', 'FEMALE': 'Female'
})
# 5. Data Type Conversion
df['totvotpoll'] = pd.to_numeric(df['totvotpoll'], errors='coerce')
df['electors'] = pd.to_numeric(df['electors'], errors='coerce')
# Final Check
print("Final Data Types:")
print(df.dtypes)
print("Cleaned Dataset Preview:")
print(df.head())
# Save the cleaned dataset
cleaned_file_path = "indian_election_cleaned.csv"
df.to_csv(cleaned_file_path, index=False)