# series  is like  1D array
import pandas as pd
import numpy as nm
# list to series pandas
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 2, 2, 4154, 4, 1524, 424, 24, 24, 24, 24, 242, 42, 424, 24, 24, 24, 24, 2,
        4242]
st = pd.Series(data)
print("new series list = \n", st)

# Numpy to series pandas
data = nm.arange(1, 20000, 5)
st = pd.Series(data)
print("new series Numpy = \n", st)

# Dictionary  to series pandas

data = {
    'Id': [1, 2 ],
    'Name': ["Al Arman Ovi", "Al Arman Ovi"],
}

st = pd.Series(data)
print("new series Dictionary = \n", st)