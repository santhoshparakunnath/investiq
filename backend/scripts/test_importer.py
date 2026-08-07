import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.importers.icici_direct_importer import ICICIDirectImporter

tradebook = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "personal"
    / "tradeBooktest.xls"
)

importer = ICICIDirectImporter()

df = importer.load(tradebook)

print(df.head())

print()
print(df.columns.tolist())