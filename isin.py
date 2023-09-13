import pandas as pd

path = "csv/NEw2.xlsx"
file = pd.read_excel(path)

# True
print(file[(file.Total.isin([240, 261, 245])) & (file.Bangla == "A+")].drop_duplicates())
# False
print("\n", file[(~(file.Total.isin([240, 261, 245])) & ~(file.Bangla == "A+"))].drop_duplicates())
