import pandas as pd

input_path = "C:/Users/Ovi/PycharmProjects/pandas_practice/csv/Salary.csv"

# Read the CSV file into a DataFrame
pds = pd.read_csv(input_path)

print("Before condition \n", pds)
pds.drop_duplicates(inplace=True)


print("after condition with and \n", pds.loc[(pds['Total'] > 100000) & (pds['Salary'] > 101301)])

print("after condition with or  \n", pds.loc[(pds['Total'] > 100000) | (pds['Salary'] > 101302.0)])

print("after condition not \n", pds.loc[~((pds['Total'] > 100000) & (pds['Salary'] > 101301))])
