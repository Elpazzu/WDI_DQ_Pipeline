import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv('C:/Users/makra/OneDrive/Desktop/WDI_Project/WDI_DQ_Pipeline/data/raw/wdi_data.csv')

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())