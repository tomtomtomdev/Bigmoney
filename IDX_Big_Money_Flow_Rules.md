# IDX Big Money / Institutional Flow Analysis Rules

## 1. Foreign Flow Analysis (Analisis Foreign Flow)

Foreign investors are considered big fund / institutional investors. Monitoring their movements is critical for understanding market direction.

**Key Metrics:**
- **Net Foreign Buy (NFB):** Foreign institutions accumulating → bullish signal
- **Net Foreign Sell (NFS):** Outflow of institutional money → bearish signal
- Strong positive correlation between NFB and IHSG gains; negative correlation between NFS and IHSG declines

**Data Sources:**
- IDX website (idx.co.id) — end-of-day foreign flow per stock
- IDX Data Services — real-time, delayed, end-of-day, and log data
- Bloomberg / Refinitiv (LSEG) — institutional-grade data
- Broker platforms: Mirae Asset, Phillip Sekuritas (POEMS), Stockbit, RTI Business

> **Note:** Since June 27, 2022, IDX closed investor domicile codes during trading hours. Foreign flow is only visible after market close.

---

## 2. Broker Flow / Broker Summary Analysis

End-of-day broker summary data is published and useful for spotting accumulation/distribution patterns from institutional-linked brokers.

**Key Signals:**
- A single broker repeatedly appearing as the largest buyer/seller on a stock
- Sudden volume spike from a known foreign broker
- Known foreign broker codes: CS (Credit Suisse), DB (Deutsche Bank), MS (Morgan Stanley), RX (Macquarie)

---

## 3. Money Flow Index (MFI) — Technical Indicator

**Formula:**
```
Typical Price = (High + Low + Close) / 3
Raw Money Flow = Typical Price × Volume
MFI = 100 - (100 / (1 + Money Flow Ratio))
```

**Signal Rules:**
- MFI > 80 → Overbought (potential distribution by institutions)
- MFI < 20 → Oversold (potential accumulation by institutions)
- Rising MFI before price increase → Early sign of institutional accumulation
- Declining MFI before price drop → Early sign of distribution
- MFI rises significantly while price is flat → Buying volume increasing, breakout potential

**Divergence Signals:**
- **Bullish divergence:** Price makes lower low, MFI makes higher low → Institutional accumulation before reversal
- **Bearish divergence:** Price makes higher high, MFI makes lower high → Smart money exiting

---

## 4. Volume & Price Action Analysis (Bandarmologi)

**Rules:**
| Pattern | Interpretation |
|---|---|
| High volume + sideways/flat price | Accumulation phase — big money quietly buying |
| High volume + price breakout | Institutional entry confirmation |
| Low volume + rising price | Weak rally, NOT institutionally backed |
| High volume + price drop + quick recovery | Shakeout — forcing weak hands out before a move up |
| Abnormal volume (3x–5x ADV) without news | Suspect institutional activity |

---

## 5. Macro & Sectoral Flow Rules

**Macro Triggers That Attract Institutional Flow:**
- Strong GDP growth, controlled inflation, stable Rupiah
- Positive political stability signals
- Rising global commodity prices (coal, nickel, palm oil) → drives flow into mining/plantation sectors
- Fed rate cuts → EM capital inflow, positive for IDX

**Macro Triggers That Repel Institutional Flow:**
- Fed rate hikes → capital outflow from EM
- Weak USD/IDR (Rupiah depreciation) → capital flight risk
- Geopolitical uncertainty or policy instability

---

## 6. MSCI / Index Rebalancing Rules

- Track quarterly MSCI Emerging Markets and FTSE rebalancing schedules
- Stocks added to MSCI EM → passive fund inflows (Vanguard, BlackRock, etc.)
- Stocks removed from MSCI EM → forced selling by passive funds
- Anticipate these flows in advance of rebalancing dates

---

## 7. Tools & Platforms

| Tool | Use Case |
|---|---|
| idx.co.id | Official end-of-day foreign flow per stock |
| Stockbit / RTI Business | Foreign flow charts, broker summary |
| Bloomberg / Refinitiv | Institutional-grade flow data |
| TradingView | MFI, volume analysis, charting |
| CNBC Indonesia / Bisnis.com | Macro sentiment & foreign flow news |

---

## Key Principles

1. **Follow the money, not the news** — institutional moves often happen before headlines
2. **Combine methods** — Foreign flow + Volume analysis + MFI gives the most reliable picture
3. **Context matters** — Net foreign buy on blue chips (BBCA, TLKM, BMRI) carries more weight than on small-cap stocks
4. **Use confluence** — Require at least 2–3 confirming signals before drawing a conclusion
5. **Don't fight the flow** — If sustained NFS is occurring on the broad market, avoid aggressive long positions
