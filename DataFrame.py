import pandas as pd

path = "I:\Pandas\pandas\csv\BDUNI.csv"
pds = pd.read_csv(path)

for index, row in pds.iterrows():
    university = row["University"]
    phd_granting = row["Ph.D. granting"]

    # Check if "Ph.D. granting" is "Yes" or "No" and print accordingly
    if phd_granting == "Yes":
        print(f"{university} --------->> {phd_granting}")
