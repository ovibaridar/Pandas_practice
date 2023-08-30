import pandas as pd

path = "C:/Users/Ovi/PycharmProjects/pandas_practice/csv/NEw.xlsx"

xl = pd.read_excel(path)

xl["Total"] = xl["Bangla"] + xl["English"] + xl["Math"]

print("Before where\n", xl)

# Use .where to change values in Bangla, English, and Math to "A+" if they are greater than 80
xl["Bangla"] = xl["Bangla"].where(xl["Bangla"] < 80, "A+")
xl["English"] = xl["English"].where(xl["English"] < 80, "A+")
xl["Math"] = xl["Math"].where(xl["Math"] < 80, "A+")

xl.to_excel("C:/Users/Ovi/PycharmProjects/pandas_practice/csv/NEw2.xlsx", index=False)

print("done and ok")
