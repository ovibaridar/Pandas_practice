import pandas as pd

# Input file path
input_path = "C:/Users/Ovi/PycharmProjects/pandas_practice/csv/Book1.xlsx"

# Read the Excel file into DataFrames for each sheet
pds = pd.read_excel(input_path, sheet_name='s1')
pds2 = pd.read_excel(input_path, sheet_name='s2')

# Print the DataFrames
print("DataFrame from 's1':")
print(pds)

print("DataFrame from 's2':")
print(pds2)

print("inner\n", pd.merge(pds, pds2, on="Name", how="inner"))
print("outer\n", pd.merge(pds, pds2, on="Name", how="outer"))
print("left\n", pd.merge(pds, pds2, on="Name", how="left"))
print("right\n", pd.merge(pds, pds2, on="Name", how="right"))

# if and only if no same column in sheets
print("\n\nif no same column")
print("inner\n", pd.merge(pds, pds2, left_on="Name", right_on="Name", how="inner"))
print("outer\n", pd.merge(pds, pds2, left_on="Name", right_on="Name", how="outer"))
print("left\n", pd.merge(pds, pds2, left_on="Name", right_on="Name", how="left"))
print("right\n", pd.merge(pds, pds2, left_on="Name", right_on="Name", how="right"))
