from pathlib import Path

import pandas as pd


class ICICIDirectImporter:
    """
    Imports ICICI Direct tradebook files.
    """

    def load(self, file_path: str | Path) -> pd.DataFrame:

        file_path = Path(file_path)

        df = pd.read_csv(
            file_path,
            sep="\t",
            engine="python"
        )

        return df