import pandas as pd

# Input file path
input_path = "I:/Pandas/pandas/csv/Book1.xlsx"

# Read the Excel file into DataFrames for each sheet
pds = pd.read_excel(input_path, sheet_name='s1')
pds2 = pd.read_excel(input_path, sheet_name='s2')

# Print the DataFrames
print("DataFrame from 's1':")
print(pds)

print("DataFrame from 's2':")
print(pds2)

pds3 = pd.concat([pds, pds2], ignore_index=True)
pds4 = pd.concat([pds, pds2], ignore_index=True, axis=1)
pds5 = pd.concat([pds, pds2], ignore_index=True, axis=0)

print("after Concat\n", pds3)
print("after Concat and axis=1\n", pds4)
print("after Concat and axis=0\n", pds5)
