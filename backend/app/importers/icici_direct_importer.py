import pandas as pd


class ICICIDirectImporter:
    """
    Reads an ICICI Direct tradebook into a DataFrame.
    """

    def load(self, file):

        df = pd.read_csv(
            file,
            sep="\t",
            engine="python"
        )

        return df