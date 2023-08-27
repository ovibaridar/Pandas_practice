import pandas as pd

# Input file path
input_path = "I:/Pandas/pandas/csv/Salary.csv"

# Read the CSV file into a DataFrame
pds = pd.read_csv(input_path)

pds = pds.fillna(20)
# pds = pds.dropna()
# Calculate the "Total" column
pds["Total"] = pds["YearsExperience"] + pds["Salary"]

# Save the modified DataFrame to a new CSV file
pds.to_csv(input_path, index=False)  # Use index=False to avoid writing row numbers as a column

print("Done.")
print(pds)
