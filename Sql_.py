import pandas as pd

import pandas as pd

path = "C:/Users/Ovi/PycharmProjects/pandas_practice/csv/NEw.xlsx"

xl = pd.read_excel(path)
print(xl)

xl = xl._append({'Name': "Tania", 'Bangla': 90, 'English': 81, 'Math': 90}, ignore_index=True)
xl = xl._append({'Name': "Koli", 'Bangla': 90, 'English': 81, 'Math': 90}, ignore_index=True)
xl = xl._append({'Name': "Koli", 'Bangla': 90, 'English': 81, 'Math': 90}, ignore_index=True)
xl = xl._append({'Name': "Toufic", 'Bangla': 90, 'English': 81, 'Math': 90}, ignore_index=True)
xl = xl._append({'Name': "Lalu", 'Bangla': 90, 'English': 81, 'Math': 90}, ignore_index=True)

xl.to_excel(path, index=False)
print(xl)
