from operator import index

import pandas as pd

from app.importers.icici_direct_mapper import ICICIDirectMapper
from app.importers.base_importer import BaseImporter
from app.validators.icici_tradebook_validator import ICICIDirectTradebookValidator


class ICICIDirectImporter(BaseImporter):
    """
    Imports an ICICI Direct tradebook.
    """
    def can_import(self, file) -> bool:
        return True

    def load(self, file):

        return pd.read_csv(
            file,
            sep="\t",
            engine="python"
        )

     

    def import_transactions(self, file):

        df = self.load(file)

        mapper = ICICIDirectMapper()
        validator = ICICIDirectTradebookValidator()

        transactions = []
        warnings = []

        for index, row in df.iterrows():

                validation_errors = validator.validate(row)
                print("Row:", index + 1)
                print("Validation Errors:", validation_errors)

                if validation_errors:

                      print(f"Row {index + 1}")

                      for error in validation_errors:
                        print(error)
                      continue

                transactions.append(
                    mapper.to_transaction(row)
                )

        return transactions