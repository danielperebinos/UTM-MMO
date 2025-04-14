import os

import pandas as pd

RAW_DIR = r"C:/Users/daniel.perebinos/Documents/Univer/MMO/Laboratorul IV/RAW"

final = pd.DataFrame()

for filename in os.listdir(RAW_DIR):
    company = filename.split("_")[0]
    df = pd.read_csv(os.path.join(RAW_DIR, filename), delimiter=";")
    df = df.sort_values(by="Date")
    final["Date"] = df["Date"]
    final[company] = df["Closing price"]

final.set_index("Date", inplace=True)
final.to_excel("nasdaq.xlsx")
