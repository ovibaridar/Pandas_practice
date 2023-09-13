import pandas as pd

product = [
    ("Apple", 20, "Bogura"),
    ("Apple", 25, "Narayanganj"),
    ("Apple", 24, "Joypurhat"),
    ("Orange", 30, "Noakhali"),
    ("Orange", 29, "Bogura"),
    ("Orange", 25, "Narayanganj"),
    ("Orange", 24, "Joypurhat"),
    ("Orange", 30, "Noakhali"),
    ("Mango", 30, "Bogura"),
    ("Mango", 25, "Narayanganj"),
    ("Mango", 24, "Joypurhat"),
    ("Mango", 30, "Noakhali"),
    ("Banana", 45, "Bogura"),
    ("Banana", 25, "Narayanganj"),
    ("Banana", 24, "Joypurhat"),
    ("Banana", 30, "Noakhali")
]

Dataset = pd.DataFrame(product, columns=["Name", "Price", "District"])
Dataset2 = Dataset.groupby("Name")
print(Dataset2[["Price", "District"]].agg(["min", "max","count"]))
print("\n done")