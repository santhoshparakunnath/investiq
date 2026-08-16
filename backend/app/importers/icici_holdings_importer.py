import pandas as pd

from app.importers.base_importer import BaseImporter
from app.importers.icici_holdings_mapper import (
    ICICIDirectHoldingsMapper,
)


class ICICIDirectHoldingsImporter:
    """
    Imports an ICICI Direct Holdings export.
    """

    def can_import(self, file) -> bool:
        return True

    def load(self, file):

        return pd.read_csv(file, sep="\t")

    def import_holdings(self, file):

        df = self.load(file)

        mapper = ICICIDirectHoldingsMapper()

        holdings = []

        for _, row in df.iterrows():

            holdings.append(
                mapper.to_holding(row)
            )

        return holdings