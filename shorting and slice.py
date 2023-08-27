import pandas as pd

# Input file path
input_path = "I:/Pandas/pandas/csv/Salary.csv"

# Read the CSV file into a DataFrame
pds = pd.read_csv(input_path)
# print(pds.columns)
# print(pds.sort_values('Total',ascending=False))
# print(pds.sort_values('Total', ascending=True))
pds = pds.sort_values('Total', ascending=True).reset_index(drop=True)
print(pds)

# print(pds['Salary'])

# head function
# print(pds.head())
# print(pds.head(3))

# tail function
# print(pds.tail())
# print(pds.tail(3))

# print specific row

# print(pds[0:10])

# print specific multiple column

print(pds.loc[1:9, ['Salary', 'Total']])
