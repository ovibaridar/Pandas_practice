import pandas as pd

path = "C:/Users/Ovi/PycharmProjects/pandas_practice/csv/BDUNI.csv"
pds = pd.read_csv(path)


# for index, row in pds.iterrows():
#     university = row["University"]
#     phd_granting = row["Ph.D. granting"]
#
#     # Check if "Ph.D. granting" is "Yes" or "No" and print accordingly
#     if phd_granting == "Yes":
#         print(f"{university} --------->> {phd_granting}")


# using DataFrame
sr = pd.DataFrame(pds)
for index, row in sr.iterrows():
    university = row["University"]
    granting = row["Ph.D. granting"]
    if granting == "Yes":
        print(university, "----------------->>>>>>>>>>>", granting)


