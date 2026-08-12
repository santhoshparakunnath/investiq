## ADR-001: Trade Value

Decision:
Store broker-reported trade_value instead of calculating it.

Reason:
The broker may calculate trade value using more precision than the displayed price, leading to small rounding differences. The imported value is the authoritative financial record.