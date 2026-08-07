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

print(f"\nRows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nColumn Names")
print("=" * 60)

for i, col in enumerate(df.columns):
    print(f"{i+1:2d}. {col}")