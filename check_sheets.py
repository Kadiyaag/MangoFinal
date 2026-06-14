import pandas as pd

print("=== TableS1.xlsx ===")
xls1 = pd.ExcelFile("data/TableS1.xlsx")
print(xls1.sheet_names)

print("\n=== TableS2.xlsx ===")
xls2 = pd.ExcelFile("data/TableS2.xlsx")
print(xls2.sheet_names)