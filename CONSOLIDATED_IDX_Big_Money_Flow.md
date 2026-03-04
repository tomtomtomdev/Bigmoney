# Consolidated Analysis: Big Money Flow Detection in the Indonesia Stock Exchange (IDX)

## Consensus & Dissent Across 9 Sources

> **Purpose:** Single reference document consolidating where all sources agree, where they meaningfully disagree, and unique contributions from each.
>
> **Date compiled:** March 2026

---

### Sources Analyzed

| # | Source | Author/Origin | Focus |
|---|--------|---------------|-------|
| 1 | `IDX_Big_Money_Flow_Rules.md` | Manual compilation | Concise rule set |
| 2 | `deepseek.md` | DeepSeek AI | Implementation protocol |
| 3 | `grok.md` | Grok AI | Practical daily trading workflow |
| 4 | `gemini.md` | Gemini AI | 8-method framework |
| 5 | `gpt.md` | GPT | Framework (identical to gemini.md) |
| 6 | `mistral.md` | Mistral AI | Regulatory + 2026 updates |
| 7 | `qwen.md` | Qwen AI | Risk management + bandarmology |
| 8 | `Indonesia_Institutional_Flow_Tracking_Methods.pdf` | Z.ai Research (2025) | Comprehensive guide |
| 9 | `indonesia_institutional_flow_analysis.pdf` | Kimi.ai | Academic/statistical guide |

> **Note:** `gemini.md` and `gpt.md` contain word-for-word identical content. Only **8 truly independent perspectives** exist.

---

## 1. UNIVERSAL CONSENSUS (All 9 Sources Agree)

These points appear in every single source document without exception:

### 1.1 Foreign Net Flow Is the #1 Indicator

Every source identifies **Net Foreign Buy/Sell (Aliran Dana Asing)** as the primary, most accessible proxy for institutional activity on IDX. The formula is universal:

```
Net Foreign Flow (NFF) = Total Foreign Buy Value - Total Foreign Sell Value
```

### 1.2 IDX Official Data Is the Gold Standard

All sources rank **idx.co.id** (and its data portal data.idx.co.id) as the top data source for institutional flow tracking. This includes broker summaries, stock summaries, and foreign flow aggregates published daily.

### 1.3 Volume-Price Confirmation Is Mandatory

No source recommends acting on flow data alone. All require **volume and price confirmation** before interpreting any flow signal as actionable.

### 1.4 Multi-Signal Confluence Required

All sources state a minimum of **2-3 confirming signals** before acting:
- Flow direction (net buy/sell)
- Volume anomaly
- Price action alignment
- Broker activity pattern

### 1.5 Institutional Brokers Are Identifiable

All sources name the same key brokers:

| Type | Brokers |
|------|---------|
| **Foreign** | UBS Sekuritas, Morgan Stanley Indonesia, CLSA Indonesia, Macquarie Securities, Credit Suisse Indonesia |
| **Domestic Institutional** | Mandiri Sekuritas, BNI Sekuritas, Danareksa Sekuritas, Trimegah Sekuritas |

### 1.6 LQ45/Blue-Chip Focus

Institutions concentrate in **high-liquidity stocks** (LQ45 and IDX30 indices). Flow signals carry significantly more weight in large-cap names where institutional participation is highest.

### 1.7 "Follow the Money, Not the News"

All sources emphasize that **institutional moves precede headlines**. By the time news reaches retail investors, institutional positioning is typically already complete.

### 1.8 Daily/Weekly/Monthly Tracking Cadence

All prescribe the same **multi-timeframe approach**:
- **Daily:** Foreign flow direction, broker summary, volume anomalies
- **Weekly:** Cumulative flow trends, sector rotation signals, broker ranking shifts
- **Monthly:** KSEI ownership data, IDX free-float reports, macro realignment

### 1.9 Flow Is a Tool, Not a Standalone System

Every source warns against using flow data as the **sole decision-maker**. It must be combined with:
- Fundamental analysis (earnings, valuation)
- Technical analysis (chart patterns, indicators)
- Risk management (position sizing, stop-losses)

### 1.10 Data Has Significant Limitations

All acknowledge:
- **Delayed reporting** (data is after-the-fact, not real-time during trading hours)
- **Incomplete picture** (broker aggregation hides individual client activity)
- **Domicile-based classification** may misidentify actual investor nationality
- **Derivatives and OTC trades** not captured in equity flow data
- **Cross-broker execution** can split large institutional orders across multiple firms

---

## 2. STRONG CONSENSUS (7+ Sources Agree)

### 2.1 The Flow-Price Signal Matrix

Agreed by 7 of 9 sources (all except Kimi.ai PDF which uses statistical models instead of this heuristic framework):

| Foreign Flow | Price Action | Signal | Action |
|-------------|-------------|--------|--------|
| Net Buy | Price Rising | **Strong confirmed uptrend** | Long / Add to position |
| Net Buy | Price Flat/Consolidating | **Quiet accumulation** | Prepare long entry (highest probability setup) |
| Net Sell | Price Rising | **Distribution / weakening** | Reduce exposure / caution |
| Net Sell | Price Falling | **Confirmed downtrend** | Avoid / go defensive |

> The "Foreign Buy + Price Flat" combination is highlighted by multiple sources as the **highest-probability** setup because it suggests institutions are accumulating before a price move that retail hasn't yet recognized.

### 2.2 Technical Indicators for Flow Detection

Agreed by 6-7 of 9 sources:

| Indicator | What It Reveals | Source Count |
|-----------|----------------|-------------|
| **OBV (On-Balance Volume)** | Cumulative volume adjusted for price direction; divergence from price signals hidden accumulation/distribution | 7/9 |
| **MFI (Money Flow Index)** | Price + volume combined; overbought/oversold with flow context | 6/9 |
| **VWAP (Volume Weighted Average Price)** | Institutional execution benchmark; trades near VWAP suggest institutional activity | 6/9 |
| **A/D Line (Accumulation/Distribution)** | Flow of money into/out of a security; rising A/D with flat price = accumulation | 6/9 |

### 2.3 Sector Rotation Monitoring

**7 of 9 sources** emphasize tracking which sectors receive consistent institutional inflow. Banking, consumer goods, and infrastructure sectors historically attract the most foreign institutional interest due to their liquidity, index weight, and growth prospects.

### 2.4 Macro Triggers Drive Foreign Flow

**7 of 9 sources** identify the same macro drivers:
- **US Federal Reserve** interest rate decisions
- **USD/IDR exchange rate** movements
- **Commodity prices** (coal, palm oil, nickel — Indonesia's key exports)
- **Global risk appetite** (risk-on vs. risk-off sentiment)
- **Bank Indonesia monetary policy** decisions

### 2.5 Never Fight Sustained Institutional Selling

**7 of 9 sources** include this as a core principle: when foreign institutions are on a sustained selling streak (5+ consecutive days), do not attempt to "buy the dip" until selling subsides and reversal signals appear.

---

## 3. MARKET-WIDE THRESHOLDS (Specific Numbers From Sources)

Where sources provide quantitative thresholds for actionable signals:

### 3.1 Net Foreign Flow Thresholds

| Threshold | Signal | Source(s) |
|-----------|--------|-----------|
| Weekly net foreign buy > **Rp 1-2 trillion** | Strong bullish signal for market | Grok, IDX Rules |
| Daily net foreign sell > **Rp 1.5-2 trillion** | Risk-off event, defensive posture warranted | Grok |
| Consistent net buy for **5-10 trading days** + rising IHSG | Accumulation confirmed | Grok, DeepSeek |

### 3.2 Volume Anomaly Detection

| Threshold | Interpretation | Source(s) |
|-----------|---------------|-----------|
| Current volume > **2x** 20-day average | Suspect institutional activity | Z.ai PDF |
| Current volume > **3-5x** average daily volume | High-confidence institutional signal | IDX Rules |
| Volume spike + price breakout above resistance | Institutional accumulation complete, breakout confirmed | Multiple sources |

### 3.3 Broker Concentration

| Threshold | Interpretation | Source(s) |
|-----------|---------------|-----------|
| Top **1-3 institutional brokers** account for >**60%** of net buy in a stock | High-conviction institutional positioning | Qwen |
| Single broker executing >**30%** of daily volume in a stock | Likely block trade or coordinated institutional execution | DeepSeek |

### 3.4 Position Sizing Rules (Qwen — Only Source With Explicit Rules)

| Rule | Detail |
|------|--------|
| Position size per trade | **2-5%** of portfolio |
| Scale-in method | **30/40/30** (initial/add/final) |
| Maximum per stock | **15%** of portfolio |
| Stop-loss | Mandatory for all flow-based entries |

---

## 4. DISSENTING OPINIONS & DISAGREEMENTS

### 4a. Which Institutions Matter Most?

**This is the most significant disagreement across all sources.**

| Position | Source(s) | Argument |
|----------|-----------|----------|
| **Foreign flow is THE primary driver** | Grok, Gemini/GPT, IDX Rules, Z.ai PDF, Mistral | Foreign investors hold 40-45% of market cap, ~70% of free-float value; their transactions have statistically significant impact on volatility and price |
| **Domestic institutions are often MORE influential** | DeepSeek | "Domestic institutional investors are often the most influential variable in market movement" — argues local pension funds, mutual funds, and insurance companies drive sustained trends |
| **Both matter equally — track the lead-lag** | Kimi.ai PDF | Academic VAR models show institutional trading (foreign + domestic) leads retail by 1-3 days; individual trading only affects other individuals, not institutions |

**Assessment:** DeepSeek stands alone in prioritizing domestic over foreign. The academic evidence (Kimi.ai) suggests both matter but through different mechanisms: foreign flow drives volatility and sentiment; domestic institutions drive sustained accumulation. The majority view (foreign as primary) reflects the reality that foreign flow data is most publicly accessible and immediately actionable.

### 4b. Quantitative Rigor: Practical vs. Statistical

| Approach | Source(s) | Methods Used |
|----------|-----------|-------------|
| **Practical/visual** | Grok, IDX Rules, Gemini/GPT | Stockbit charts, eyeball flow direction, daily checklists, broker summary screenshots |
| **Rules-based with thresholds** | Qwen, DeepSeek | Specific numeric rules (3-5 day consistency, percentage thresholds, 6-point checklists) |
| **Academic/statistical** | Kimi.ai PDF | VAR models, Granger causality tests, LSV herding measure, Newey-West covariance estimation, impulse response functions |

**Assessment:** This is a fundamental methodological divide. Most sources are practical retail trading guides; only Kimi.ai brings formal statistical rigor. Neither approach is "wrong" — they serve different users:
- **Retail day/swing traders** → Practical approach (Grok, IDX Rules)
- **Systematic/rule-based traders** → Threshold approach (Qwen, DeepSeek)
- **Quant analysts/researchers** → Statistical approach (Kimi.ai)

### 4c. Bandarmology: Legitimate Tool or Risky Practice?

"Bandarmology" refers to the Indonesian practice of identifying and following market makers/manipulators ("bandar") based on broker summary data.

| Position | Source(s) |
|----------|-----------|
| **Valid analysis tool with explicit checklist** | Qwen (6-point checklist; warns "only proceed if 5/6 conditions pass") |
| **Implicit in methodology** (uses broker tracking without the term) | Grok, IDX Rules |
| **Not mentioned at all** | Mistral, Z.ai PDF, Kimi.ai PDF, Gemini/GPT |

**Qwen's 6-Point Bandarmology Checklist:**
1. Consistent broker accumulation pattern (3+ days)
2. Volume confirms (above average)
3. Price technically sound (not overextended)
4. No negative fundamental catalysts
5. Sector momentum supports
6. Risk/reward ratio acceptable

**Assessment:** The more "institutional/academic" sources avoid the term entirely. Qwen provides the most balanced treatment — acknowledges utility but explicitly warns about:
- **Manipulation risk** (the "bandar" may deliberately create misleading patterns)
- **Illiquidity traps** (following into small-cap, illiquid stocks)
- **Regulatory scrutiny** (OJK investigations into market manipulation)

### 4d. Market Structure Numbers (Contradictory Data)

Different sources cite different numbers that appear contradictory but actually measure different things:

| Metric | Source | Number |
|--------|--------|--------|
| Foreign share of transaction **VALUE** | DeepSeek | ~36% |
| Foreign share of market **CAPITALIZATION** | Z.ai PDF | 40-45% |
| Foreign share of **FREE-FLOAT** | Z.ai PDF | ~70% |
| Institutional equity **OWNERSHIP** | Kimi.ai PDF | 93-94% |
| Individual trading **VALUE** share | Kimi.ai PDF | ~34% |
| Retail share of **TRANSACTIONS** (count) | DeepSeek | ~50% |

**Assessment:** These are not true disagreements — they measure different things:
- **Institutions OWN most of the market** (93-94% of equity ownership)
- **But retail generates disproportionate TRADING ACTIVITY** (~34-50% of transactions by count/value)
- **Foreign investors' share of free-float (~70%) far exceeds their share of total market cap (~40-45%)** because many Indonesian companies have concentrated ownership by founding families/SOEs
- **Flow analysis targets the institutional 60-66% of trading value**, which is where the directional signals live

### 4e. Ownership Disclosure Threshold

| Rule | Source(s) |
|------|-----------|
| **5% ownership** triggers disclosure | Gemini/GPT |
| **1% threshold** (effective March 2026) | Mistral |

**Assessment:** Mistral has the most current regulatory information. The **1% rule is a major 2026 reform** that reduced the threshold from 5% to align with international standards after an MSCI warning. Other sources were written before this change. The 1% threshold significantly improves transparency and institutional flow tracking capability. Reports must be submitted within 5 working days (transitioning to 3 days with electronic reporting).

---

## 5. UNIQUE CONTRIBUTIONS BY SOURCE

Each source offers at least one insight not found (or not emphasized) in the others:

| Source | Unique Contribution |
|--------|-------------------|
| **IDX Rules** | IDX closed investor domicile codes during trading hours since **June 27, 2022** — foreign flow data is only visible after market close, not intraday. This is a critical operational detail for anyone trying to track flow in real-time. |
| **DeepSeek** | **Herding behavior recognition rule** — when multiple institutional brokers simultaneously shift to the same side (all buying or all selling), it signals coordinated institutional positioning that indicates either trend initiation or trend exhaustion. |
| **Grok** | **Most practical daily routine** with specific timing tied to Jakarta market hours: pre-market check at 07:30-08:30 WIB, intraday monitoring, and post-close review. Total daily time commitment: 5-10 minutes. |
| **Mistral** | **2026 regulatory updates**: 1% disclosure threshold, 15% minimum free-float requirement (up from 7.5%), KSEI expansion to 27 investor sub-types. Includes **comparative analysis** with Singapore, Malaysia, and Thailand regulatory frameworks. |
| **Qwen** | **Only source with explicit position sizing rules** (2-5% per trade, 30/40/30 scale-in, max 15% per stock) and the **only detailed bandarmology checklist** with pass/fail criteria. |
| **Kimi.ai PDF** | **Academic formulas and statistical methods**: Institutional Herding Index (H = \|B/(B+S) - p\| - E\|B/(B+S) - p\|), Flow-Adjusted Momentum (FAM = Price Momentum x Institutional Flow Direction), VAR modeling for lead-lag analysis, and the finding of **asymmetric market impact** (institutional trading affects both investor types; retail only affects other retail). |
| **Z.ai PDF** | **Most structured decision-making framework** — a 6-step process: (1) Confirm flow signals across multiple sources → (2) Assess magnitude and duration → (3) Consider market context and drivers → (4) Evaluate alignment with fundamentals and technicals → (5) Determine position sizing based on conviction → (6) Establish entry, exit, and stop-loss levels. |
| **Gemini/GPT** | **Order book / Level II data analysis** — discusses large bid/ask walls, iceberg orders, and odd-lot patterns as indicators of institutional activity. This order-book microstructure analysis is not covered in depth by other sources. |

---

## 6. SYNTHESIZED MASTER RULES

### 6.1 Ten Core Detection Rules

Distilled from consensus across all sources:

**Rule 1: Track Net Foreign Flow Daily**
Monitor aggregate NFF from IDX data. Sustained direction (5+ days) matters more than any single day.

**Rule 2: Confirm With Volume**
Flow signals require volume confirmation. Volume > 2x the 20-day average in the direction of flow = institutional involvement likely.

**Rule 3: Use the Flow-Price Matrix**
Cross-reference flow direction with price action. The strongest signal is "Foreign Buy + Price Flat" (quiet accumulation before a move).

**Rule 4: Monitor Institutional Broker Activity**
Track the top 5-10 brokers by value daily. When foreign brokers (UBS, Morgan Stanley, CLSA, Macquarie) dominate the buy side, institutional accumulation is underway.

**Rule 5: Watch for Broker Concentration**
If 1-3 institutional brokers account for >60% of net buying in a stock, it's a high-conviction institutional position.

**Rule 6: Never Fight Sustained Institutional Selling**
When foreign institutions sell for 5+ consecutive days with increasing volume, do not attempt to buy the dip. Wait for reversal signals.

**Rule 7: Track Sector Rotation**
Institutional money rotates between sectors. When consistent inflows shift from one sector to another over 2-4 weeks, it signals a strategic reallocation.

**Rule 8: Factor In Macro Context**
Foreign flow is driven by global macro (Fed policy, USD/IDR, commodity prices, risk appetite). Flow signals in line with macro trends are higher probability.

**Rule 9: Use Multi-Timeframe Analysis**
Daily flow for timing, weekly flow for trend confirmation, monthly flow for strategic direction. Don't trade daily noise — wait for weekly confirmation.

**Rule 10: Flow Is One Input, Not the Only Input**
Always combine flow analysis with fundamental valuation, technical chart patterns, and risk management. No single data source is sufficient.

### 6.2 Data Sources Ranked by Reliability

| Rank | Source | Data Type | Access | Cost |
|------|--------|-----------|--------|------|
| 1 | **IDX (idx.co.id / data.idx.co.id)** | Broker summaries, foreign flow, stock data | Public | Free |
| 2 | **KSEI (ksei.co.id)** | Investor registration, ownership data, 27-type classification | Public/Semi-public | Free |
| 3 | **OJK (ojk.go.id)** | Regulatory filings, 1% ownership disclosures, enforcement | Public | Free |
| 4 | **Broker Platforms (Stockbit, IPOT, Ajaib, Mirae HOTS)** | Real-time visualization, broker summary tools, community insights | Account required | Free-Premium |
| 5 | **Financial News (IDNFinancials, Kontan, Bisnis Indonesia)** | Flow commentary, institutional transaction reports, sector analysis | Public | Free-Subscription |

### 6.3 Consolidated Daily/Weekly/Monthly Workflow

#### Daily Routine (5-15 minutes)

**Pre-Market (07:00-08:30 WIB):**
- Review overnight global markets (US, Europe, Asia)
- Check USD/IDR movement and commodity prices
- Note any macro events (Fed, Bank Indonesia, economic data releases)

**During Market Hours (09:00-15:00 WIB):**
- Monitor real-time price and volume for watchlist stocks
- Watch for unusual volume spikes (>2x average)
- Note block trades through institutional brokers
- *Remember: Foreign flow domicile data is NOT available intraday (closed since June 2022)*

**Post-Close (15:30-16:30 WIB):**
- Check final daily foreign flow numbers from IDX
- Review broker summary: who bought, who sold, how much
- Update cumulative flow tracker
- Apply Flow-Price Matrix to key positions
- Log observations in trading journal

#### Weekly Review (30-60 minutes, weekend)

- Calculate 5-day cumulative foreign flow by market and by stock
- Analyze broker ranking changes (institutional vs. retail broker shifts)
- Assess sector flow trends (where is money rotating?)
- Cross-reference with weekly IHSG performance
- Backtest any flow signals from the week against actual price action
- Review OJK filings for ownership changes

#### Monthly Deep Dive (1-2 hours)

- Download official IDX foreign investor report
- Review KSEI ownership structure changes
- Update institutional ownership database for key holdings
- Analyze herding behavior statistics (are institutions clustering?)
- Recalibrate any quantitative models (VAR parameters, flow thresholds)
- Review strategy performance: which rules had the highest predictive value?
- Check for regulatory changes (OJK, IDX rule updates)

### 6.4 Risk Management Rules

Consolidated from Qwen (primary source), Z.ai PDF, and other sources:

| Rule | Detail |
|------|--------|
| **Position sizing** | 2-5% of portfolio per flow-based trade |
| **Scale-in approach** | 30% initial → 40% on confirmation → 30% on breakout |
| **Maximum single-stock exposure** | 15% of portfolio |
| **Stop-loss** | Mandatory for every position; set before entry |
| **Diversification** | Spread across multiple stocks and sectors |
| **Flow reversal exit** | If institutional flow reverses direction for 3+ consecutive days against your position, reduce or exit |
| **Never risk more than you can verify** | If you cannot confirm the flow signal from at least 2 independent data sources, reduce position size by 50% |

### 6.5 Known Limitations & Caveats

Every user of institutional flow analysis must understand these limitations:

1. **Foreign flow ≠ all institutional flow.** Domestic institutions (pension funds, mutual funds, insurance) are not separately identified in daily broker summaries.

2. **Broker aggregation hides individuals.** A single broker code represents all clients — retail and institutional mixed together. Only the broker knows the breakdown.

3. **Domicile ≠ nationality.** Foreign flow is classified by transaction domicile input, not actual investor identity. A foreign-domiciled entity could be Indonesian-controlled, and vice versa.

4. **Delayed data.** Most flow data is available only after market close. Intraday foreign flow has been unavailable since IDX closed domicile codes during trading hours in June 2022.

5. **T+2 settlement lag.** Settlement timing creates mismatches between trade date and actual ownership transfer.

6. **Derivatives and OTC invisible.** Equity flow data does not capture hedging activity through derivatives, options, or over-the-counter transactions.

7. **Cross-broker execution.** Large institutions routinely split orders across multiple brokers to minimize market impact, making any single broker's data an incomplete picture.

8. **Institutions can be wrong.** Institutional trades do not always represent superior information. They may trade for reasons unrelated to fundamentals (redemptions, rebalancing, mandate constraints).

9. **Flow strategies degrade with popularity.** As more market participants follow the same flow signals, the signals become crowded and less effective.

10. **Regime changes alter patterns.** Market crises (2008, COVID-19) and regulatory changes fundamentally alter institutional behavior. Historical patterns may not apply in new regimes.

---

## 7. ACADEMIC FRAMEWORK (From Kimi.ai PDF)

For users seeking quantitative/statistical rigor beyond practical heuristics:

### 7.1 Key Formulas

**Institutional Herding Index (LSV Measure):**
```
H = |B/(B+S) - p| - E|B/(B+S) - p|

Where:
  B = number of institutional buyers in stock i during period t
  S = number of institutional sellers
  p = expected proportion under null hypothesis of random trading
  E[.] = expected value adjustment factor
```

**Flow-Adjusted Momentum (FAM):**
```
FAM = Price Momentum × Institutional Flow Direction
```
Combines price trend with institutional flow to create a composite signal.

### 7.2 Key Academic Findings

| Finding | Implication |
|---------|------------|
| Institutional trading leads retail by **1-3 days** (VAR model) | There is a predictive window for observing institutional moves before retail follows |
| Individual trading affects **only other individuals**, not institutions | Retail noise does not influence smart money; institutions are independent actors |
| Institutional buying has **asymmetric market impact** | The price impact of institutional buying is different from selling; markets respond asymmetrically |
| Institutions follow **momentum strategies**; retail follows **contrarian** | Institutions buy into rising prices; retail buys dips. This explains the lead-lag relationship. |
| Banks/insurance are **pressure-sensitive**; mutual/pension funds are **pressure-insensitive** | Different institution types respond differently to market pressure — track them separately if data permits |

### 7.3 Market Structure Statistics

| Metric | Value | Implication |
|--------|-------|------------|
| Individual equity ownership | 6-7% | Retail owns very little of the market despite high trading activity |
| Institutional equity ownership | 93-94% | Institutions are the dominant long-term holders |
| Individual trading value share | ~34% | Retail generates disproportionate trading activity relative to ownership |
| Institutional trading value share | ~66% | Institutional trades are larger but less frequent |
| Average institutional trade value | ~IDR 863 billion | vs. IDR 6.35 billion for individuals — 136x larger |

---

## 8. REGULATORY LANDSCAPE (2026 Updates from Mistral)

### 8.1 Key 2026 Reforms

| Reform | Detail | Impact on Flow Tracking |
|--------|--------|------------------------|
| **1% ownership disclosure** | Down from 5%; must report within 5 working days | Much earlier visibility into institutional accumulation; lower threshold catches more position building |
| **15% minimum free-float** | Up from 7.5%; phased over 1-2 years | 267 companies must increase float; ~$11B in shares released to public; more shares available for institutional flow signals |
| **27 KSEI investor sub-types** | Expanded from 9 categories | Better granularity in distinguishing global institutions from intermediaries, pension funds from mutual funds |
| **Electronic reporting (SPE)** | Moving to 3-day deadline | Faster disclosure = faster flow signal detection |

### 8.2 Regional Comparison

| Market | Disclosure Threshold | Free-Float Min | Electronic Reporting | Flow Tracking Maturity |
|--------|---------------------|----------------|---------------------|----------------------|
| **Indonesia** | 1% (2026) | 15% (phasing in) | In progress | Improving rapidly |
| **Singapore** | 5% | Higher effective | Advanced | Most mature |
| **Malaysia** | 5% | Varies | Advanced | Mature |
| **Thailand** | 5% | Varies | Moderate | Moderate |

Indonesia's 1% threshold is now the **most stringent in ASEAN**, positioning it for significantly improved institutional transparency.

---

## 9. SOURCE RELIABILITY ASSESSMENT

| Source | Strengths | Weaknesses | Best For |
|--------|-----------|------------|----------|
| **IDX Rules** | Concise, practical, IDX-specific operational details | No statistical backing; no risk management | Quick reference card |
| **DeepSeek** | Implementation-focused, herding behavior insight | Controversial domestic > foreign claim; lacks citations | Systematic rule implementation |
| **Grok** | Most practical daily routine, time-efficient | Light on theory; no academic rigor | Daily trading workflow |
| **Gemini/GPT** | Broad 8-method coverage, order book analysis | Identical content (not independent); outdated 5% threshold | Comprehensive method overview |
| **Mistral** | Most current regulatory data (2026); regional comparison | Less trading-oriented; more regulatory/policy focus | Regulatory compliance, macro view |
| **Qwen** | Only source with position sizing + bandarmology checklist | Bandarmology is controversial; may encourage risky small-cap speculation | Risk management, bandarmology users |
| **Z.ai PDF** | Most structured decision framework; well-organized | Broad coverage but lacks quantitative depth | Decision-making framework, new practitioners |
| **Kimi.ai PDF** | Academic rigor; VAR models; herding index; statistical formulas | Not accessible to most retail traders; requires quantitative background | Quant analysis, research |

---

## 10. QUICK REFERENCE: DECISION FLOWCHART

```
START: Check daily net foreign flow from IDX
  │
  ├─ Net Foreign BUY?
  │   ├─ Volume > 2x average? ──YES──┐
  │   │                               │
  │   └─ Volume normal? ──── WAIT ────┤
  │                                    │
  │   Institutional brokers dominant? ─┤
  │   ├─ YES ──── HIGH CONVICTION ─────┤
  │   └─ NO ───── MODERATE SIGNAL ─────┤
  │                                    │
  │   Apply Flow-Price Matrix:         │
  │   ├─ Price UP ── Confirmed trend ──┤──► Consider LONG
  │   ├─ Price FLAT ── Accumulation ───┤──► Prepare to BUY (best setup)
  │   └─ Price DOWN ── Divergence ─────┤──► WAIT for confirmation
  │
  ├─ Net Foreign SELL?
  │   ├─ 5+ consecutive days? ─────────┤──► DO NOT BUY; go DEFENSIVE
  │   ├─ Price still rising? ──────────┤──► DISTRIBUTION warning; REDUCE
  │   └─ Price falling + volume up? ───┤──► Confirmed DOWNTREND; AVOID
  │
  └─ FLAT / Mixed signals?
      └─ No clear direction ───────────┤──► WAIT; do not force trades
                                       │
  ALWAYS: Check macro context (Fed, USD/IDR, commodities)
  ALWAYS: Confirm with ≥2 data sources
  ALWAYS: Apply position sizing rules (2-5% per trade, max 15% per stock)
  ALWAYS: Set stop-loss before entry
```

---

## Appendix: Glossary of Key Terms

| Term | Definition |
|------|-----------|
| **NFF (Net Foreign Flow)** | Total foreign buy value minus total foreign sell value; the primary institutional flow indicator |
| **Broker Summary** | Daily aggregate trading data published by IDX showing volume and value per broker per stock |
| **Bandarmology** | Indonesian practice of identifying market makers ("bandar") through broker summary patterns |
| **IHSG (JCI)** | Jakarta Composite Index; main benchmark for IDX overall market performance |
| **LQ45** | Index of 45 most liquid stocks on IDX; primary institutional trading universe |
| **KSEI** | Kustodian Sentral Efek Indonesia; central securities depository managing investor data |
| **OJK** | Otoritas Jasa Keuangan; Indonesia's Financial Services Authority (regulator) |
| **IDX30** | Index of 30 largest, most liquid stocks on IDX |
| **Free-float** | Shares available for public trading (excluding locked-up shares held by founders/controlling shareholders) |
| **Block trade** | Large single transaction, typically institutional, executed outside the regular order book |
| **VAR (Vector Autoregression)** | Statistical model estimating how past values of multiple variables predict current values |
| **LSV Measure** | Lakonishok-Shleifer-Vishny herding measure; quantifies whether institutions are buying/selling the same stocks |
| **FAM (Flow-Adjusted Momentum)** | Composite signal combining price momentum with institutional flow direction |
| **OBV (On-Balance Volume)** | Technical indicator tracking cumulative volume adjusted for price direction |
| **MFI (Money Flow Index)** | Technical indicator combining price and volume to identify overbought/oversold conditions |
| **VWAP** | Volume Weighted Average Price; institutional execution benchmark |
| **A/D Line** | Accumulation/Distribution Line; measures money flow into/out of a security |

---

*This document consolidates 9 source documents (7 AI-generated markdown files + 2 PDF research papers) into a single reference. Individual source files are preserved for audit. The 1% ownership disclosure rule and 15% free-float requirement reflect March 2026 regulations.*

*Document Version: 1.0*
*Compiled: March 2026*
