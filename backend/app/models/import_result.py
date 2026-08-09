from dataclasses import dataclass, field

from app.models.import_summary import ImportSummary
from app.models.transaction import Transaction


@dataclass
class ImportResult:
    """
    Complete result of an import operation.
    """

    summary: ImportSummary

    transactions: list[Transaction] = field(default_factory=list)

    from app.models.import_warning import ImportWarning

    warnings: list[ImportWarning] = field(default_factory=list)

    errors: list[str] = field(default_factory=list)