import sys
from pathlib import Path

# Add the backend folder to Python's import path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.portfolio.loader import ExcelLoader

excel_file = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "personal"
    / "tradebook.xlsx"
)

loader = ExcelLoader(excel_file)

df = loader.load()

print("\nFirst 5 rows")
print("-" * 50)
print(df.head())

print("\nColumns")
print("-" * 50)
print(df.columns.tolist())

print("\nShape")
print("-" * 50)
print(df.shape)