import pandas as pd
# Input file path
input_path = "C:/Users/Ovi/PycharmProjects/pandas_practice/csv/Salary.csv"
# Read the CSV file into a DataFrame
pds = pd.read_csv(input_path)
print(pds.duplicated())
print("After change duplicate ------------------>")
pds.drop_duplicates(inplace=True)
print(pds.duplicated())
