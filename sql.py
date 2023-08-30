import pandas as pd

path = "C:/Users/Ovi/PycharmProjects/pandas_practice/csv/NEw2.xlsx"

xl = pd.read_excel(path)
print("Before filtered \n", xl)

# Use double square brackets [[]] to select specific columns
filtered_data = xl[((xl['Bangla'] == 'A+') | (xl['English'] == 'A+') | (xl['Math'] == 'A+')) & (xl['Total'] >= 240)]

# Select specific columns for the filtered rows
result = filtered_data[['Name', 'Bangla', 'English', 'Math', 'Total']]

print("After filtered \n", result)
