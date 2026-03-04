# 📄 Institutional Flow Tracking Rules - Indonesia Stock Market (IDX)
*Markdown File - Copy & Save as `idx_institutional_flow_rules.md`*

```markdown
# 📊 Institutional/Big Money Flow Tracking Rules
## Indonesia Stock Exchange (IDX) - Analysis Framework

> **Disclaimer**: This document is for educational purposes only. Not financial advice. Always verify data with official IDX/OJK sources.

---

## 🔑 Core Data Sources

### Official IDX Resources
- **Broker Summary**: `idx.co.id/en/market-data/trading-summary/broker-summary`
- **Foreign Flow Statistics**: Daily net buy/sell by foreign investors
- **RDIS Educational Portal**: Official IDX learning resources

### Key Data Points to Monitor
| Data Field | Description | Why It Matters |
|------------|-------------|---------------|
| Broker Code | F-series (foreign), D-series (domestic institutional) | Identifies player type |
| Net Buy/Sell Value | Total buy value minus sell value (IDR) | Shows directional pressure |
| Average Buy/Sell Price | Weighted avg execution price | Reveals institutional entry zone |
| Transaction Frequency | Number of trades per broker | Distinguishes block trades vs retail churn |
| Foreign Net Flow | Aggregate foreign investor activity | Leading indicator for blue-chip moves |

---

## 📐 Core Analysis Rules

### ✅ Rule 1: Confirm Consistency Over Time
```
✔ LOOK FOR: Same institutional broker(s) net buying 3-5 consecutive sessions
✘ AVOID: Reacting to single-day spikes without follow-through
```
*Rationale*: Institutional accumulation is a process, not a one-off event.

### ✅ Rule 2: Price vs. Average Buy Price Comparison
```
IF Current Price ≤ Institutional Avg Buy Price + 3% 
→ Potential entry zone with margin of safety

IF Current Price ≥ Institutional Avg Buy Price + 15% 
→ Wait for pullback; risk of chasing
```

### ✅ Rule 3: Volume Confirmation Triangulation
```
Strong Signal = Price ↑ + Volume ↑ + Institutional Net Buy ↑
Weak Signal = Price ↑ + Volume ↓ + Institutional Net Sell (distribution warning)
```

### ✅ Rule 4: Broker Concentration Filter
```
HIGH CONVICTION: Top 1-3 institutional brokers control >60% of net buy volume
LOW CONVICTION: Net buy scattered across 10+ mixed broker types (retail noise)
```

### ✅ Rule 5: Foreign Flow Context for LQ45 Stocks
```
For LQ45/Blue-Chip Stocks:
• Foreign Net Buy + Price Consolidation = Accumulation signal
• Foreign Net Sell + Price Rally = Distribution warning
• Neutral Foreign Flow + Domestic Institutional Buy = Local fund rotation
```

---

## 🔄 Market Phase Identification Framework

### Phase 1: ACCUMULATION
```
Characteristics:
□ Price: Sideways/low volatility near support
□ Volume: Below average, occasional spikes
□ Broker Activity: Institutional net buy, retail net sell
□ Action: Watchlist, prepare entry, small position sizing
```

### Phase 2: MARK-UP
```
Characteristics:
□ Price: Higher highs, higher lows, breakout above resistance
□ Volume: Increasing on up-days, declining on pullbacks
□ Broker Activity: Institutional participation visible, foreign inflow
□ Action: Add to position, trail stop-loss, take partial profits at targets
```

### Phase 3: DISTRIBUTION
```
Characteristics:
□ Price: Choppy, failed breakouts, lower highs
□ Volume: High volume on down-days, divergence on rallies
□ Broker Activity: Institutional net sell into strength, retail net buy
□ Action: Reduce exposure, tighten stops, avoid new longs
```

### Phase 4: MARK-DOWN
```
Characteristics:
□ Price: Lower lows, breakdown below support
□ Volume: Spike on breakdown, then declining
□ Broker Activity: Broad-based selling, foreign outflow
□ Action: Stay defensive, wait for accumulation signals
```

---

## ⚠️ Critical Risk Management Rules

### Position Sizing
```
• Max 2-5% portfolio risk per "flow signal" trade
• Scale in: 30% initial entry, 40% on confirmation, 30% on breakout
• Never allocate >15% portfolio to single stock regardless of flow strength
```

### Entry/Exit Discipline
```
ENTRY CONDITIONS (ALL must be met):
☑ Institutional net buy consistency (3+ days)
☑ Price at technical support/breakout level
☑ Volume confirmation (>20-day average)
☑ No major negative catalyst pending

EXIT TRIGGERS (ANY triggers review):
☒ Price drops below institutional avg buy price by >5%
☒ Institutional broker flips to net sell for 2 consecutive days
☒ Volume spike on down-day with broker distribution pattern
☒ Fundamental deterioration (earnings miss, governance issue)
```

### Common Pitfalls to Avoid
```
❌ "Big broker buy = guaranteed profit" → Brokers execute for multiple clients with conflicting strategies
❌ Ignoring market regime → Accumulation in bear market takes longer; adjust expectations
❌ Overfitting patterns → Not every broker concentration leads to breakout; use probability thinking
❌ Confirmation bias → Don't ignore bearish technicals because "big money is buying"
❌ Late entry → By the time retail sees obvious flow, institutions may be distributing
```

---

## 🎯 Bandarmology-Specific Guidelines (Local Context)

### What is Bandarmology?
*Indonesian term for analyzing "bandar" (market maker/big player) behavior through transaction patterns.*

### Valid Applications
```
✓ Identifying low-float stocks with concentrated institutional activity
✓ Spotting unusual price-volume divergences that precede moves
✓ Understanding liquidity dynamics in mid/small-cap IDX stocks
```

### Limitations & Warnings
```
⚠ Not a standalone system: Must combine with technical/fundamental analysis
⚠ Manipulation risk: Concentrated flow can be temporary or misleading
⚠ Regulatory scrutiny: Abnormal patterns may trigger OJK/IDX investigations
⚠ Liquidity risk: Following "bandar" into illiquid stocks can trap retail investors
```

### Bandarmology Checklist
```
[ ] Is net buy concentrated in ≤3 institutional broker codes?
[ ] Is average buy price tightly clustered (suggesting coordinated accumulation)?
[ ] Does volume profile support the flow narrative (not just price noise)?
[ ] Is the stock at a logical technical level (support, breakout, retest)?
[ ] Are there fundamental/macro catalysts aligning with the flow?
[ ] Is float/liquidity sufficient for your intended position size?
→ Only proceed if ≥5/6 checks pass
```

---

## 📱 Daily Workflow Template

```markdown
## [DATE] IDX Institutional Flow Check

### Watchlist Stocks Analysis
| Stock | Top Net Buyer Broker | Net Value (IDR) | Avg Buy Price | Current Price | Foreign Flow | Signal |
|-------|---------------------|-----------------|---------------|---------------|--------------|--------|
| BBCA  | Fxxx / Dxxx         | +X.XB           | 9,850         | 9,900         | +Net Buy     | ✅ Watch |
| TLKM  | ...                 | ...             | ...           | ...           | ...          | ...    |

### Decision Framework
1. **Signal Strength**: [Strong/Moderate/Weak] based on rule checklist
2. **Technical Alignment**: [Support/Breakout/Overextended/Neutral]
3. **Risk Assessment**: [Low/Medium/High] based on volatility & liquidity
4. **Action**: [Enter/Add/Reduce/Wait/Avoid] + Position size % 

### Notes
- Key catalysts this week: [Earnings, policy, macro events]
- Market regime: [Bullish/Neutral/Bearish] based on JCI trend
- Personal bias check: [Am I forcing a signal due to FOMO?]
```

---

## 📚 Reference & Verification Sources

### Primary Sources (Always Verify Here First)
- Indonesia Stock Exchange: https://www.idx.co.id
- OJK (Financial Services Authority): https://www.ojk.go.id
- IDX RDIS Educational Portal: https://rdis.idx.co.id

### Secondary Tools (Convenience, Not Primary)
- Stockbit, IPOT, Ajaib apps (broker summary visualization)
- IDN Financials, Kontan, Bisnis Indonesia (flow news aggregation)
- Kiwoom Sekuritas, Mirae Asset HOTS (institutional-grade terminals)

### Academic/Research References
- "Fundamental, Technical and Broker Summary Analysis in Indonesian Stock Market" (Journal of Indonesian Capital Market Studies)
- OJK Working Paper: "Investor Behavior and Trading Strategies in Emerging Markets"
- IDX Research: "Foreign Investor Flow and Market Volatility in IDX"

---

## 🔄 Maintenance & Updates

```
✅ Review this framework quarterly for:
• IDX rule changes (broker reporting, foreign ownership limits)
• New data sources or analytical tools
• Personal performance review: Which rules had highest predictive value?

✅ Update watchlist methodology when:
• Market regime shifts (bull → bear or vice versa)
• Sector rotation changes institutional focus
• Personal risk tolerance or capital allocation changes
```

---

> **Final Principle**: *"Broker Summary = Alat bantu, bukan penentu tunggal"*  
> (Broker Summary = A supporting tool, not a sole determinant)  
> — IDX RDIS Educational Materials

*Last Updated: [DATE]*  
*Version: 1.0*
```

---

## 💾 How to Save This File

1. **Copy** all content between the triple backticks (```markdown ... ```)
2. **Paste** into a text editor (VS Code, Notepad++, Sublime Text, etc.)
3. **Save As**: `idx_institutional_flow_rules.md`
4. **Optional**: Add to your trading journal folder or Git repository for version control

## 🔄 Pro Tips for Using This MD File

```bash
# View in terminal (Linux/Mac)
less idx_institutional_flow_rules.md

# Convert to PDF (with pandoc)
pandoc idx_institutional_flow_rules.md -o idx_rules.pdf

# Track changes with Git
git init && git add idx_institutional_flow_rules.md && git commit -m "Initial flow rules"
```

> ✅ **Done!** You now have a portable, searchable, version-controllable reference for IDX institutional flow analysis. Update the `[DATE]` placeholders and customize the watchlist template to match your trading style.

*Need updates? Re-run this analysis quarterly or when IDX announces new market data protocols.* 🚀
