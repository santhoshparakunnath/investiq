from fastapi import UploadFile

from app.importers.icici_direct_importer import ICICIDirectImporter
from app.models.import_result import ImportResult
from app.models.import_summary import ImportSummary


class ImportService:

    def import_file(self, file: UploadFile):

        importer = ICICIDirectImporter()

        transactions = importer.import_transactions(file.file)

        if transactions:
            first_trade_date = min(t.trade_date for t in transactions)
            last_trade_date = max(t.trade_date for t in transactions)
        else:
            first_trade_date = None
            last_trade_date = None

        summary = ImportSummary(
            broker="ICICI Direct",
            transaction_count=len(transactions),
            first_trade_date=first_trade_date,
            last_trade_date=last_trade_date,
        )

        return ImportResult(
            summary=summary,
            transactions=transactions,
        )