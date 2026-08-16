from pathlib import Path
from decimal import Decimal

from app.importers.icici_direct_importer import ICICIDirectImporter
from app.importers.icici_holdings_importer import ICICIDirectHoldingsImporter
from app.repositories.corporate_action_repository import CorporateActionRepository
from app.services.portfolio_reconciliation_service import PortfolioReconciliationService


# ---------------------------------------------------------
# File paths
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

TRADEBOOK_FILE = BASE_DIR / "data" / "imports" / "ICICI_tradebook_15yr.txt"
HOLDINGS_FILE = BASE_DIR / "data" / "imports" / "holdings.txt"
CORPORATE_ACTIONS_FILE = BASE_DIR / "data" / "corporate_actions.json"


# ---------------------------------------------------------
# Import data
# ---------------------------------------------------------

print("\nLoading tradebook...")

tradebook_importer = ICICIDirectImporter()
transactions = tradebook_importer.import_data(TRADEBOOK_FILE)

print(f"Transactions: {len(transactions)}")


print("\nLoading holdings...")

holdings_importer = ICICIDirectHoldingsImporter()
holdings = holdings_importer.import_holdings(HOLDINGS_FILE)

print(f"Holdings: {len(holdings)}")


print("\nLoading corporate actions...")

corporate_action_repository = CorporateActionRepository(
    CORPORATE_ACTIONS_FILE
)

corporate_actions = corporate_action_repository.get_all()

print(f"Corporate actions: {len(corporate_actions)}")


# ---------------------------------------------------------
# Reconcile
# ---------------------------------------------------------

print("\nRunning reconciliation...")

service = PortfolioReconciliationService()

results = service.reconcile(
    transactions=transactions,
    holdings=holdings,
    corporate_actions=corporate_actions,
)


# ---------------------------------------------------------
# Display results
# ---------------------------------------------------------

print("\n" + "=" * 90)
print("PORTFOLIO RECONCILIATION")
print("=" * 90)

print(
    f"{'Symbol':<10}"
    f"{'Calculated':>15}"
    f"{'Actual':>15}"
    f"{'Difference':>15}"
    f"{'Status':<30}"
)

print("-" * 90)

for result in results:
    print(
        f"{result.symbol:<10}"
        f"{result.calculated_quantity:>15}"
        f"{result.actual_quantity:>15}"
        f"{result.difference:>15}"
        f"{result.status.value:<30}"
    )

    if result.explanation:
        print(f"    {result.explanation}")


# ---------------------------------------------------------
# Summary
# ---------------------------------------------------------

print("\n" + "=" * 90)
print("SUMMARY")
print("=" * 90)

status_counts = {}

for result in results:
    status = result.status.value
    status_counts[status] = status_counts.get(status, 0) + 1

for status, count in sorted(status_counts.items()):
    print(f"{status:<30} {count}")


print("\nReconciliation complete.")