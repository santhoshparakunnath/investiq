# InvestIQ Product Roadmap

**Version:** 1.0  
**Status:** Active  
**Last Updated:** 10-Aug-2026

---

# Purpose

This document describes the planned evolution of InvestIQ.

The roadmap is organised around investor questions rather than technical features.

Every phase should increase InvestIQ's ability to understand investors and help them make better investment decisions.

---

# Product Evolution

InvestIQ evolves through five stages.

```
Collect

↓

Measure

↓

Understand

↓

Explain

↓

Coach
```

---

# Phase 1 — Foundation ✅

Objective

Create a stable platform capable of importing and validating investment data.

Completed

## Import Engine

- ICICI Direct Tradebook Import
- ICICI Direct Holdings Import
- Validation Framework
- Mapping Framework

## Domain Models

- Transaction
- Holding
- TradeLot
- Charges
- ImportResult
- ImportSummary
- PortfolioSummary
- InvestmentDNA

## Services

- ImportService
- PortfolioService
- InvestmentDNAService

## Testing

- Validators
- Importers
- Services

---

# Phase 2 — Portfolio Intelligence

Question

> What do I own today?

Capabilities

- Portfolio Summary
- Portfolio Value
- Current Holdings
- Sector Allocation
- Asset Allocation
- Portfolio Concentration
- Market Value Analysis
- Cash Allocation

Outcome

InvestIQ understands the investor's current portfolio.

---

# Phase 3 — Investment DNA

Question

> Who am I as an investor?

Capabilities

- Years Investing
- Buy Count
- Sell Count
- Companies Invested
- Current Holdings
- Most Traded Stock
- Average Holding Period
- Average Position Size
- Trading Frequency

Outcome

InvestIQ understands the investor's overall profile.

---

# Phase 4 — Behaviour Intelligence

Question

> How do I invest?

Capabilities

## Buying Behaviour

- Averaging Down
- Averaging Up
- Staggered Buying
- Lump Sum Investing
- Buying During Corrections
- Buying During Rallies

## Selling Behaviour

- Profit Booking
- Stop Loss Behaviour
- Partial Selling
- Complete Exit Behaviour
- Panic Selling

## Holding Behaviour

- Average Holding Period
- Longest Holding
- Shortest Holding
- Winners vs Losers

## Risk Behaviour

- Concentration
- Diversification
- Position Sizing
- Cash Utilisation
- Sector Bias

Outcome

InvestIQ understands investor behaviour.

---

# Phase 5 — Performance Intelligence

Question

> Which decisions created wealth?

Capabilities

- Win Rate
- Loss Rate
- Average Winner
- Average Loser
- Largest Winner
- Largest Loser
- Performance by Sector
- Performance by Holding Period
- Performance by Market Conditions

Outcome

InvestIQ understands historical investment performance.

---

# Phase 6 — Insight Engine

Question

> What patterns exist?

Capabilities

Generate evidence-backed observations.

Examples

- Your best investments were held longer than three years.
- You consistently outperform after market corrections.
- You frequently sell winning investments too early.
- Your highest conviction investments generate the strongest returns.

Outcome

Facts become knowledge.

---

# Phase 7 — Recommendation Engine

Question

> What should I consider before making this decision?

Capabilities

Generate personalised recommendations using:

- Historical Behaviour
- Investment DNA
- Portfolio Context
- Risk Profile
- Previous Decisions

Recommendations always include supporting evidence.

Outcome

InvestIQ begins coaching investors.

---

# Phase 8 — AI Coach

Question

> Can I discuss my investments naturally?

Capabilities

Natural language conversations.

Examples

"I'm thinking about buying Infosys."

"What mistakes have I repeated?"

"What has changed in my investing over the last five years?"

The AI Coach explains findings produced by the Intelligence Engine.

The AI Coach never replaces deterministic analytics.

Outcome

InvestIQ becomes a conversational investment companion.

---

# Future Expansion

Potential future capabilities include:

- Live Market Data
- Broker Integrations
- Mutual Funds
- ETFs
- Bonds
- Gold
- International Investments
- Family Portfolios
- Advisor Mode
- Mobile Applications
- Portfolio Alerts
- Tax Analysis
- Goal Planning

These are intentionally outside the MVP.

---

# MVP Definition

The first public release of InvestIQ should allow an investor to:

- Import historical trades.
- Import current holdings.
- View portfolio summary.
- View Investment DNA.
- Understand buying behaviour.
- Understand selling behaviour.
- Understand risk profile.
- Receive at least five evidence-backed insights.
- Ask natural language questions about their investment history.

If these objectives are achieved, InvestIQ delivers meaningful value even without advanced AI features.

---

# Development Principles

Every roadmap item should satisfy all of the following.

- Solves a real investor problem.
- Produces measurable value.
- Is deterministic.
- Is testable.
- Can be explained using evidence.
- Moves InvestIQ closer to its vision.

---

# Guiding Principle

We do not build features because they are technically interesting.

We build capabilities because they help investors make better decisions.

Every roadmap item should strengthen the Intelligence Engine.

Everything else builds upon it.