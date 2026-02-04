import warnings
warnings.simplefilter("ignore")

import os
import pandas as pd

# 🎯 EXACT LINE (case-insensitive)
TARGET_LINE = "75383"

input_path = input(
    "Enter folder path (example: D:\\Year Wise Work\\2025): "
).strip()

if not os.path.exists(input_path):
    print("❌ Path does not exist.")
    exit()

# parent folder bhi include hoga
parent_path = os.path.dirname(input_path)
paths_to_scan = {input_path, parent_path}

def search_excel(file_path):
    try:
        excel = pd.ExcelFile(file_path)
        for sheet in excel.sheet_names:
            df = excel.parse(sheet, dtype=str)

            # har cell ko strip + lowercase
            cleaned = df.applymap(
                lambda x: str(x).strip().lower()
            )

            # EXACT match
            if (cleaned == TARGET_LINE).any().any():
                print(f"FOUND ✅  File: {file_path} | Sheet: {sheet}")
                return
    except Exception:
        pass

print("\nScanning started...\n")

for path in paths_to_scan:
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith((".xlsx", ".xls")):
                search_excel(os.path.join(root, file))

print("\nScan completed.")
