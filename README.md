# Bigmoney — IDX Big Money Flow Screener

A real-time stock screener for the Indonesia Stock Exchange (IDX) that detects institutional and foreign money flow patterns. It aggregates multiple screening strategies, enriches each stock with fundamental and flow data, and produces a composite score to surface high-conviction institutional activity.

## How It Works

Bigmoney runs six screeners against the IDX via the Stockbit API, then enriches and scores every stock that appears:

### Screeners

| Category | Screener | What It Detects |
|----------|----------|-----------------|
| Big Money | 1 Month Net Foreign Flow | Stocks with >10B IDR net foreign inflow and >1B daily value |
| Big Money | Big Accumulation | Bandar accumulation/distribution score >20 with >3B daily value |
| Big Money | Bandar Accumulation Uptrend | Rising bandar value above MA20, with MA10 > MA20 |
| Big Money | Insider Net Buy (3M-1Y) | Consistent insider net buying across 3-month, 6-month, and 1-year windows |
| Value | PE Below Mean | PE ratio below -1 standard deviation (5-year) with positive earnings |
| Value | Low P/E Stock | PE < 10 with ROE > 7% and positive book value |

### Scoring

Each stock receives two sub-scores:

- **Big Money Score (0-50)**: Based on screener hits, daily foreign flow direction, top broker identity, institutional broker concentration, and accumulation patterns (flat price + foreign buy).
- **Value Score (0-50)**: Based on screener hits, PE ratio, PBV, ROE, net income, EPS growth, and analyst consensus.

The **Total Score (0-100)** ranks stocks by combined institutional interest and fundamental value.

### Enrichment Data

For every detected stock, the app fetches:

- Company info (name, sector, market cap, price)
- Key financial ratios (PE, PBV, ROE, dividend yield, EPS growth)
- Foreign/domestic flow (daily net foreign buy/sell)
- Broker summary (top brokers, institutional broker percentage) — daily and 7-day
- Price performance (1D, 1W, 1M, etc.)
- Analyst consensus and target price

### Analytical Framework

Results include signals drawn from multiple analytical perspectives:

- **Flow signals**: Strong Uptrend, Quiet Accumulation, Distribution Warning, Confirmed Downtrend
- **Herding detection**: Flags when multiple institutional screeners fire simultaneously
- **Lead-lag analysis**: Identifies institutional accumulation phases before retail follow-through
- **Flow-Adjusted Momentum (FAM)**: Confirms or flags divergence between price movement and institutional flow

## Tech Stack

- **Backend**: Python, FastAPI, aiohttp, SSE (Server-Sent Events) for real-time scan progress
- **Frontend**: Single-page HTML/JS with a dark-themed UI
- **Data source**: Stockbit API (requires a valid token)

## Setup

### Prerequisites

- Python 3.9+
- A Stockbit account token

### Quick Start

```bash
# Clone the repo
git clone <repo-url> && cd Bigmoney

# Run (creates venv, installs deps, starts server)
./run.sh
```

Or manually:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/uvicorn bigmoney:app --host 0.0.0.0 --port 8000 --reload
```

Open `http://localhost:8000` in your browser.

### Configuration

1. Click **Settings** in the top-right corner of the UI
2. Paste your Stockbit authorization token (the app will prepend `Bearer ` if needed)
3. Click **Save**

The token is stored locally in `config.json`.

## Project Structure

```
bigmoney.py              # FastAPI app — screeners, API client, scoring engine
templates/index.html     # Frontend UI (single-page app)
requirements.txt         # Python dependencies
run.sh                   # One-command launcher
config.json              # Stockbit token (created on first save, gitignored)
results.json             # Cached scan results (created after first scan)
```

## License

This project is for personal/educational use. The screener data is sourced from Stockbit and IDX; usage is subject to their respective terms of service.
