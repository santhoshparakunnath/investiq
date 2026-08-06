from pathlib import Path

import pandas as pd


class ExcelLoader:
    """Loads portfolio data from the broker Excel workbook."""

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load(self):
        """Return transactions and holdings dataframes."""

        workbook = pd.ExcelFile(self.file_path)

        sheet = workbook.sheet_names[0]

        df = pd.read_excel(
            self.file_path,
            sheet_name=sheet
        )

        return df