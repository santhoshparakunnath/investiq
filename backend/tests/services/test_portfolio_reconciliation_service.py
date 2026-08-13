from datetime import date
from decimal import Decimal
from types import SimpleNamespace

from app.models.enums import TransactionType
from app.models.reconciliation import ReconciliationStatus
from app.services.portfolio_reconciliation_service import (
    PortfolioReconciliationService,
)


def make_transaction(symbol, action, quantity, trade_date):
    return SimpleNamespace(
        symbol=symbol,
        action=action,
        quantity=Decimal(quantity),
        trade_date=trade_date,
    )


def make_holding(symbol, quantity):
    return SimpleNamespace(
        symbol=symbol,
        quantity=quantity,
    )


def test_reconciles_calculated_position_against_current_holding():

    transactions = [
        make_transaction(
            "TATSTE",
            TransactionType.BUY,
            100,
            date(2021, 4, 6),
        ),
    ]

    holdings = [
        make_holding("TATSTE", 100),
    ]

    results = PortfolioReconciliationService().reconcile(
        transactions=transactions,
        holdings=holdings,
        corporate_actions=[],
    )

    assert len(results) == 1
    assert results[0].symbol == "TATSTE"
    assert results[0].calculated_quantity == Decimal("100")
    assert results[0].actual_quantity == Decimal("100")
    assert results[0].status == ReconciliationStatus.RECONCILED