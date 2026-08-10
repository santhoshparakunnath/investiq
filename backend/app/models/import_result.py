from dataclasses import dataclass, field

from app.models.import_summary import ImportSummary
from app.models.transaction import Transaction
from app.models.importwarning import ImportWarning


@dataclass
class ImportResult:
    """
    Complete result of an import operation.
    """

    summary: ImportSummary

    transactions: list[Transaction] = field(default_factory=list)

    warnings: list[ImportWarning] = field(default_factory=list)

    errors: list[str] = field(default_factory=list)