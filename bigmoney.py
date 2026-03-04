"""Bigmoney — IDX Big Money Flow Stock Screener."""

import asyncio
import json
import logging
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

import aiohttp
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sse_starlette.sse import EventSourceResponse

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("bigmoney")

app = FastAPI(title="Bigmoney")
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))

CONFIG_PATH = Path(__file__).parent / "config.json"
RESULTS_PATH = Path(__file__).parent / "results.json"

BASE_URL = "https://exodus.stockbit.com"

COMMON_HEADERS = {
    "accept": "*/*",
    "x-appversion": "3.19.1",
    "x-devicetype": "iPhone 11",
    "x-platform": "iOS",
    "user-agent": (
        "Stockbit/3.19.1 (stockbit.com.stockbit; build:39144; iOS 18.1.1) "
        "Alamofire/5.9.0"
    ),
    "accept-language": "ID",
    "accept-encoding": "identity",
}

# Known institutional broker codes
INSTITUTIONAL_BROKERS = {
    "UB": "UBS Sekuritas",
    "MS": "Morgan Stanley",
    "CL": "CLSA Indonesia",
    "MQ": "Macquarie Securities",
    "CS": "Credit Suisse",
    "MU": "Mandiri Sekuritas",
    "NI": "BNI Sekuritas",
    "DR": "Danareksa Sekuritas",
    "TF": "Trimegah Sekuritas",
    "GR": "CGS-CIMB",
    "JP": "J.P. Morgan",
    "RX": "Macquarie",
    "YU": "Mirae Asset",
    "KZ": "Deutsche Securities",
    "BK": "BCA Sekuritas",
    "PD": "Indo Premier",
}

# ── Screener definitions ─────────────────────────────────────────────────────

SCREENERS = {
    80: {
        "id": "80",
        "name": "1 Month Net Foreign Flow",
        "category": "big_money",
        "body": {
            "screenerid": "80",
            "name": "1 Month Net Foreign Flow",
            "description": "",
            "type": "TEMPLATE_TYPE_GURU",
            "universe": json.dumps({"name": "IHSG", "scope": "IHSG", "scopeID": "0"}),
            "sequence": "13580,16454",
            "ordertype": "desc",
            "ordercol": 2,
            "limit": 25,
            "save": "0",
            "filters": json.dumps([
                {"type": "basic", "item1": 13580, "item1_name": "1 Month Net Foreign Flow",
                 "operator": ">", "item2": "10000000000", "item2_name": "", "multiplier": "0"},
                {"type": "basic", "item1": 16454, "item1_name": "Value MA 20",
                 "operator": ">", "item2": "1000000000", "item2_name": "", "multiplier": "0"},
            ]),
        },
    },
    92: {
        "id": "92",
        "name": "Big Accumulation",
        "category": "big_money",
        "body": {
            "screenerid": "92",
            "name": "Big Accumulation",
            "description": "",
            "type": "TEMPLATE_TYPE_GURU",
            "universe": json.dumps({"scopeID": "0", "scope": "IHSG", "name": "IHSG"}),
            "sequence": "14400,13620",
            "ordertype": "desc",
            "ordercol": 2,
            "limit": 25,
            "save": "0",
            "filters": json.dumps([
                {"type": "basic", "item1": 14400, "item1_name": "Bandar Accum/Dist",
                 "operator": ">", "item2": "20", "item2_name": "", "multiplier": "0"},
                {"type": "basic", "item1": 13620, "item1_name": "Value",
                 "operator": ">", "item2": "3000000000", "item2_name": "", "multiplier": "0"},
            ]),
        },
    },
    96: {
        "id": "96",
        "name": "Bandar Accumulation Uptrend",
        "category": "big_money",
        "body": {
            "screenerid": "96",
            "name": "Bandar Accumulation Uptrend",
            "description": "",
            "type": "TEMPLATE_TYPE_GURU",
            "universe": json.dumps({"scope": "IHSG", "name": "IHSG", "scopeID": "0"}),
            "sequence": "14399,14426,16454,14425,14424",
            "ordertype": "desc",
            "ordercol": 4,
            "limit": 25,
            "save": "0",
            "filters": json.dumps([
                {"type": "compare", "item1": 14399, "item1_name": "Bandar Value",
                 "operator": ">", "item2": "14426", "item2_name": "Bandar Value MA 20",
                 "multiplier": "1"},
                {"type": "basic", "item1": 16454, "item1_name": "Value MA 20",
                 "operator": ">", "item2": "1000000000", "item2_name": "", "multiplier": "0"},
                {"type": "compare", "item1": 14425, "item1_name": "Previous Bandar Value",
                 "operator": "<=", "item2": "14399", "item2_name": "Bandar Value",
                 "multiplier": "1"},
                {"type": "compare", "item1": 14424, "item1_name": "Bandar Value MA 10",
                 "operator": ">", "item2": "14426", "item2_name": "Bandar Value MA 20",
                 "multiplier": "1"},
            ]),
        },
    },
    117: {
        "id": "117",
        "name": "Insider Net Buy (3M-1Y)",
        "category": "big_money",
        "body": {
            "screenerid": "117",
            "name": "Insider Net Buy (3M - 1Y)",
            "description": "",
            "type": "TEMPLATE_TYPE_GURU",
            "universe": json.dumps({"scope": "IHSG", "name": "IHSG", "scopeID": "0"}),
            "sequence": "21366,16456,21365,21367",
            "ordertype": "desc",
            "ordercol": 5,
            "limit": 25,
            "save": "0",
            "filters": json.dumps([
                {"type": "basic", "item1": 21366, "item1_name": "Net Insider Buy / Sell (6M) (%)",
                 "operator": ">", "item2": "0", "multiplier": "0", "item2_name": ""},
                {"type": "basic", "item1": 21366, "item1_name": "Net Insider Buy / Sell (6M) (%)",
                 "operator": "<", "item2": "100", "multiplier": "0", "item2_name": ""},
                {"type": "basic", "item1": 16456, "item1_name": "Value MA 100",
                 "operator": ">", "item2": "500000000", "multiplier": "0", "item2_name": ""},
                {"type": "basic", "item1": 21365, "item1_name": "Net Insider Buy / Sell (3M) (%)",
                 "operator": ">", "item2": "0", "multiplier": "0", "item2_name": ""},
                {"type": "basic", "item1": 21367, "item1_name": "Net Insider Buy / Sell (1Y) (%)",
                 "operator": ">", "item2": "0", "multiplier": "0", "item2_name": ""},
                {"type": "compare", "item1": 21366,
                 "item1_name": "Net Insider Buy / Sell (6M) (%)",
                 "operator": ">=", "item2": "21365",
                 "item2_name": "Net Insider Buy / Sell (3M) (%)", "multiplier": "1"},
            ]),
        },
    },
    27: {
        "id": "27",
        "name": "PE Below Mean",
        "category": "value",
        "body": {
            "screenerid": "27",
            "name": "PE Below Mean",
            "description": "",
            "type": "TEMPLATE_TYPE_GURU",
            "universe": json.dumps({"name": "IHSG", "scopeID": "0", "scope": "IHSG"}),
            "sequence": "2891,16462,12634,12637,3063,12464",
            "ordertype": "asc",
            "ordercol": 2,
            "limit": 25,
            "save": "0",
            "filters": json.dumps([
                {"type": "compare", "item1": 2891, "item1_name": "Current PE Ratio (TTM)",
                 "operator": "<", "item2": "16462",
                 "item2_name": "-1 PE Standard Deviation (5 Year)", "multiplier": "1"},
                {"type": "basic", "item1": 2891, "item1_name": "Current PE Ratio (TTM)",
                 "operator": ">", "item2": "0", "item2_name": "", "multiplier": "0"},
                {"type": "basic", "item1": 2891, "item1_name": "Current PE Ratio (TTM)",
                 "operator": "<=", "item2": "50", "item2_name": "", "multiplier": "0"},
                {"type": "basic", "item1": 12634,
                 "item1_name": "-1 PE Standard Deviation (3 Year)",
                 "operator": ">", "item2": "0", "item2_name": "", "multiplier": "0"},
                {"type": "basic", "item1": 12637,
                 "item1_name": "-2 PE Standard Deviation (3 Year)",
                 "operator": ">", "item2": "-10", "item2_name": "", "multiplier": "0"},
                {"type": "basic", "item1": 3063, "item1_name": "Net Income (TTM)",
                 "operator": ">", "item2": "0", "item2_name": "", "multiplier": "0"},
                {"type": "basic", "item1": 12464, "item1_name": "Volume MA 20",
                 "operator": ">", "item2": "500000", "item2_name": "", "multiplier": "0"},
            ]),
        },
    },
    107: {
        "id": "107",
        "name": "Low P/E Stock",
        "category": "value",
        "body": {
            "screenerid": "107",
            "name": "Low P/E Stock",
            "description": "",
            "type": "TEMPLATE_TYPE_GURU",
            "universe": json.dumps({"scopeID": "0", "name": "IHSG", "scope": "IHSG"}),
            "sequence": "2891,3063,1490,13439,3202,12464",
            "ordertype": "asc",
            "ordercol": 2,
            "limit": 25,
            "save": "0",
            "filters": json.dumps([
                {"type": "basic", "item1": 2891, "item1_name": "Current PE Ratio (TTM)",
                 "operator": "<", "item2": "10", "item2_name": "", "multiplier": "0"},
                {"type": "basic", "item1": 3063, "item1_name": "Net Income (TTM)",
                 "operator": ">", "item2": "0", "item2_name": "", "multiplier": "0"},
                {"type": "basic", "item1": 1490, "item1_name": "Book Value (Quarter)",
                 "operator": ">", "item2": "0", "item2_name": "", "multiplier": "0"},
                {"type": "basic", "item1": 13439, "item1_name": "Average (RoE 3 yr)",
                 "operator": ">", "item2": "7", "item2_name": "", "multiplier": "0"},
                {"type": "basic", "item1": 3202,
                 "item1_name": "Non-Operating Income (Growth: YTD YoY)",
                 "operator": "<", "item2": "25", "item2_name": "", "multiplier": "0"},
                {"type": "basic", "item1": 12464, "item1_name": "Volume MA 20",
                 "operator": ">", "item2": "100", "item2_name": "", "multiplier": "0"},
            ]),
        },
    },
}


# ── Config helpers ────────────────────────────────────────────────────────────

def load_config() -> dict:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text())
    return {}


def save_config(cfg: dict):
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2))


def get_token() -> Optional[str]:
    return load_config().get("stockbit_token")


# ── API Client ────────────────────────────────────────────────────────────────

RATE_LIMIT = asyncio.Semaphore(5)  # max 5 concurrent requests


async def api_get(session: aiohttp.ClientSession, path: str,
                  params: Optional[dict] = None) -> Optional[dict]:
    async with RATE_LIMIT:
        url = f"{BASE_URL}{path}"
        try:
            async with session.get(url, params=params) as resp:
                if resp.status == 200:
                    return await resp.json()
                log.warning("GET %s → %s", url, resp.status)
                return None
        except Exception as e:
            log.error("GET %s error: %s", url, e)
            return None


async def api_post(session: aiohttp.ClientSession, path: str,
                   body: dict) -> Optional[dict]:
    async with RATE_LIMIT:
        url = f"{BASE_URL}{path}"
        try:
            async with session.post(url, json=body) as resp:
                if resp.status == 200:
                    return await resp.json()
                log.warning("POST %s → %s", url, resp.status)
                return None
        except Exception as e:
            log.error("POST %s error: %s", url, e)
            return None


def make_session(token: str) -> aiohttp.ClientSession:
    headers = {**COMMON_HEADERS, "authorization": token}
    return aiohttp.ClientSession(headers=headers)


# ── Screener fetching ─────────────────────────────────────────────────────────

async def fetch_screener(session: aiohttp.ClientSession,
                         screener: dict) -> List[str]:
    """Fetch all pages of a screener, return list of ticker symbols."""
    tickers: List[str] = []
    page = 1
    while True:
        body = {**screener["body"], "page": page}
        data = await api_post(session, "/screener/templates", body)
        if not data:
            break
        rows = (data.get("data") or {}).get("rows") or []
        if not rows:
            break
        for row in rows:
            sym = row.get("symbol") or row.get("ticker")
            if sym:
                tickers.append(sym)
        # If fewer results than limit, we've reached the end
        if len(rows) < screener["body"].get("limit", 25):
            break
        page += 1
        await asyncio.sleep(0.2)
    return tickers


# ── Enrichment ────────────────────────────────────────────────────────────────

async def enrich_stock(session: aiohttp.ClientSession,
                       symbol: str) -> Dict[str, Any]:
    """Fetch all enrichment data for a single stock."""
    info_task = api_get(session, f"/emitten/{symbol}/info")
    stats_task = api_get(session, f"/keystats/ratio/v1/{symbol}",
                         {"year_limit": "10"})
    flow_task = api_get(
        session,
        f"/findata-view/foreign-domestic/v1/chart-data/{symbol}",
        {"market_type": "MARKET_TYPE_REGULAR", "period": "PERIOD_RANGE_1D"},
    )
    broker_task = api_get(session, f"/marketdetectors/{symbol}", {
        "investor_type": "1", "limit": "10", "market_board": "2",
        "period": "BROKER_SUMMARY_PERIOD_LATEST", "transaction_type": "1",
    })
    broker7d_task = api_get(session, f"/marketdetectors/{symbol}", {
        "investor_type": "1", "limit": "10", "market_board": "2",
        "period": "BROKER_SUMMARY_PERIOD_LAST_7_DAYS", "transaction_type": "1",
    })
    perf_task = api_get(
        session, f"/company-price-feed/price-performance/{symbol}"
    )
    analyst_task = api_get(session, f"/analyst-ratings/{symbol}/consensus")

    info, stats, flow, broker, broker7d, perf, analyst = await asyncio.gather(
        info_task, stats_task, flow_task, broker_task, broker7d_task,
        perf_task, analyst_task,
    )

    return {
        "info": info,
        "stats": stats,
        "flow": flow,
        "broker": broker,
        "broker7d": broker7d,
        "perf": perf,
        "analyst": analyst,
    }


# ── Data extraction helpers ───────────────────────────────────────────────────

def safe_float(val, default=0.0) -> float:
    if val is None:
        return default
    try:
        return float(val)
    except (TypeError, ValueError):
        return default


def extract_info(data: Optional[dict]) -> dict:
    if not data:
        return {}
    d = data.get("data") or data
    return {
        "name": d.get("company_name") or d.get("name") or "",
        "sector": d.get("sector") or d.get("sub_industry") or "",
        "market_cap": safe_float(d.get("market_cap")),
        "price": safe_float(d.get("price") or d.get("last_price")),
    }


def extract_stats(data: Optional[dict]) -> dict:
    if not data:
        return {}
    d = data.get("data") or data
    # keystats returns ratio arrays — grab the latest year
    ratios = d if isinstance(d, dict) else {}
    pe_list = ratios.get("pe") or []
    pbv_list = ratios.get("pbv") or []
    roe_list = ratios.get("roe") or []
    dy_list = ratios.get("dy") or []
    eps_list = ratios.get("eps") or []
    ni_list = ratios.get("net_income") or ratios.get("ni") or []

    def latest(lst):
        if not lst:
            return None
        # could be list of dicts or list of values
        if isinstance(lst[-1], dict):
            return lst[-1].get("value") or lst[-1].get("v")
        return lst[-1]

    def prev(lst):
        if not lst or len(lst) < 2:
            return None
        if isinstance(lst[-2], dict):
            return lst[-2].get("value") or lst[-2].get("v")
        return lst[-2]

    eps_now = safe_float(latest(eps_list))
    eps_prev = safe_float(prev(eps_list))
    eps_growth = ((eps_now - eps_prev) / abs(eps_prev) * 100) if eps_prev else 0

    return {
        "pe": safe_float(latest(pe_list)),
        "pbv": safe_float(latest(pbv_list)),
        "roe": safe_float(latest(roe_list)),
        "dy": safe_float(latest(dy_list)),
        "eps": eps_now,
        "eps_growth": eps_growth,
        "net_income": safe_float(latest(ni_list)),
    }


def extract_foreign_flow(data: Optional[dict]) -> dict:
    if not data:
        return {"net_foreign": 0, "foreign_buy": 0, "foreign_sell": 0}
    d = data.get("data") or data
    # chart-data returns arrays; take the latest entry
    items = d.get("items") or d.get("chart_data") or []
    if isinstance(d, dict) and not items:
        # try flat structure
        return {
            "net_foreign": safe_float(d.get("net_val") or d.get("net_foreign")),
            "foreign_buy": safe_float(d.get("foreign_buy") or d.get("buy_val")),
            "foreign_sell": safe_float(d.get("foreign_sell") or d.get("sell_val")),
        }
    if items:
        last = items[-1] if isinstance(items, list) else items
        if isinstance(last, dict):
            return {
                "net_foreign": safe_float(
                    last.get("net_val") or last.get("net_foreign") or last.get("value")
                ),
                "foreign_buy": safe_float(last.get("foreign_buy") or last.get("buy_val")),
                "foreign_sell": safe_float(last.get("foreign_sell") or last.get("sell_val")),
            }
    return {"net_foreign": 0, "foreign_buy": 0, "foreign_sell": 0}


def extract_broker(data: Optional[dict]) -> dict:
    if not data:
        return {"top_broker": "", "top_broker_val": 0, "brokers": [],
                "institutional_pct": 0}
    d = data.get("data") or data
    rows = d.get("rows") or d.get("brokers") or d.get("data") or []
    if isinstance(rows, dict):
        rows = rows.get("rows") or []

    brokers = []
    total_val = 0
    inst_val = 0
    for row in rows[:10]:
        code = row.get("broker_code") or row.get("code") or ""
        val = safe_float(row.get("net_val") or row.get("value") or row.get("total"))
        name = INSTITUTIONAL_BROKERS.get(code, code)
        is_inst = code in INSTITUTIONAL_BROKERS
        brokers.append({"code": code, "name": name, "value": val,
                        "is_institutional": is_inst})
        total_val += abs(val)
        if is_inst:
            inst_val += abs(val)

    inst_pct = (inst_val / total_val * 100) if total_val else 0
    top = brokers[0] if brokers else {"code": "", "name": "", "value": 0,
                                       "is_institutional": False}
    return {
        "top_broker": f"{top['code']} ({top['name']})" if top["code"] else "",
        "top_broker_val": top["value"],
        "top_broker_is_institutional": top.get("is_institutional", False),
        "brokers": brokers,
        "institutional_pct": round(inst_pct, 1),
    }


def extract_performance(data: Optional[dict]) -> dict:
    if not data:
        return {}
    d = data.get("data") or data
    result = {}
    perfs = d.get("performances") or d.get("price_performance") or d
    if isinstance(perfs, list):
        for p in perfs:
            period = p.get("period") or p.get("label") or ""
            pct = safe_float(p.get("percent_change") or p.get("change") or p.get("value"))
            result[period] = pct
    elif isinstance(perfs, dict):
        for k, v in perfs.items():
            result[k] = safe_float(v)
    return result


def extract_analyst(data: Optional[dict]) -> dict:
    if not data:
        return {"consensus": "", "target_price": 0, "num_analysts": 0}
    d = data.get("data") or data
    return {
        "consensus": d.get("consensus") or d.get("rating") or "",
        "target_price": safe_float(
            d.get("target_price") or d.get("consensus_target_price")
        ),
        "num_analysts": int(safe_float(d.get("total") or d.get("num_analysts") or 0)),
    }


# ── Scoring engine ────────────────────────────────────────────────────────────

def compute_scores(symbol: str, screener_hits: Dict[int, bool],
                   enrichment: dict) -> dict:
    """
    Compute Big Money Score (0-50) and Value Score (0-50).
    Returns dict with bm_score, value_score, total_score, and breakdown.
    """
    info = extract_info(enrichment.get("info"))
    stats = extract_stats(enrichment.get("stats"))
    flow_data = extract_foreign_flow(enrichment.get("flow"))
    broker_data = extract_broker(enrichment.get("broker"))
    broker7d = extract_broker(enrichment.get("broker7d"))
    perf = extract_performance(enrichment.get("perf"))
    analyst = extract_analyst(enrichment.get("analyst"))

    bm_breakdown = []
    bm = 0

    # Big Money Score (0-50)
    if screener_hits.get(80):
        bm += 10
        bm_breakdown.append("Foreign Flow screener (+10)")
    if screener_hits.get(92):
        bm += 8
        bm_breakdown.append("Big Accumulation screener (+8)")
    if screener_hits.get(96):
        bm += 7
        bm_breakdown.append("Bandar Uptrend screener (+7)")
    if screener_hits.get(117):
        bm += 5
        bm_breakdown.append("Insider Net Buy screener (+5)")
    if flow_data["net_foreign"] > 0:
        bm += 5
        bm_breakdown.append("Foreign flow positive today (+5)")
    if broker_data["top_broker_is_institutional"]:
        bm += 5
        bm_breakdown.append("Top broker is institutional (+5)")
    if broker_data["institutional_pct"] > 60:
        bm += 5
        bm_breakdown.append(f"Institutional concentration {broker_data['institutional_pct']}% (+5)")
    # Accumulation pattern: price flat + foreign buy
    price_change_1d = perf.get("1D") or perf.get("1d") or perf.get("1_day") or 0
    if abs(safe_float(price_change_1d)) < 2 and flow_data["net_foreign"] > 0:
        bm += 5
        bm_breakdown.append("Accumulation pattern: flat price + foreign buy (+5)")

    val_breakdown = []
    val = 0

    # Value Score (0-50)
    if screener_hits.get(27):
        val += 10
        val_breakdown.append("PE Below Mean screener (+10)")
    if screener_hits.get(107):
        val += 8
        val_breakdown.append("Low P/E screener (+8)")
    if 0 < stats.get("pe", 999) < 15:
        val += 7
        val_breakdown.append(f"PE {stats['pe']:.1f} < 15 (+7)")
    if 0 < stats.get("pbv", 999) < 1.5:
        val += 5
        val_breakdown.append(f"PBV {stats['pbv']:.2f} < 1.5 (+5)")
    if stats.get("roe", 0) > 10:
        val += 5
        val_breakdown.append(f"ROE {stats['roe']:.1f}% > 10% (+5)")
    if stats.get("net_income", 0) > 0:
        val += 5
        val_breakdown.append("Net Income positive (+5)")
    if stats.get("eps_growth", 0) > 0:
        val += 5
        val_breakdown.append(f"EPS growth {stats['eps_growth']:.1f}% (+5)")
    consensus = analyst.get("consensus", "").lower()
    if consensus in ("buy", "strong buy", "strong_buy", "overweight"):
        val += 5
        val_breakdown.append(f"Analyst consensus: {analyst['consensus']} (+5)")

    # Determine flow signal
    net_f = flow_data["net_foreign"]
    pc = safe_float(price_change_1d)
    if net_f > 0 and pc > 1:
        flow_signal = "Strong Uptrend"
    elif net_f > 0 and abs(pc) <= 1:
        flow_signal = "Quiet Accumulation"
    elif net_f < 0 and pc > 1:
        flow_signal = "Distribution Warning"
    elif net_f < 0 and pc < -1:
        flow_signal = "Confirmed Downtrend"
    else:
        flow_signal = "Neutral"

    # Unique contributions (which source rules apply)
    unique = []
    if screener_hits.get(80) and flow_data["net_foreign"] > 0:
        unique.append({
            "source": "IDX Rules",
            "signal": "Foreign accumulation confirmed — NFF > 10B + positive daily flow",
        })
    if broker_data["institutional_pct"] > 60:
        unique.append({
            "source": "Qwen (Bandarmology)",
            "signal": f"Broker concentration {broker_data['institutional_pct']}% > 60% threshold — high-conviction institutional position",
        })
    if screener_hits.get(92) and screener_hits.get(96):
        unique.append({
            "source": "DeepSeek (Herding)",
            "signal": "Both Big Accumulation + Bandar Uptrend active — potential herding behavior (multiple brokers moving same direction)",
        })
    if abs(pc) < 2 and net_f > 0:
        unique.append({
            "source": "Grok (Daily Workflow)",
            "signal": "Foreign Buy + Price Flat — highest-probability accumulation setup",
        })
    if analyst.get("consensus", "").lower() in ("buy", "strong buy", "strong_buy"):
        unique.append({
            "source": "Z.ai (Decision Framework)",
            "signal": f"Analyst consensus '{analyst['consensus']}' with target Rp{analyst.get('target_price', 0):,.0f} — fundamental alignment confirmed",
        })
    if screener_hits.get(117):
        unique.append({
            "source": "Mistral (Regulatory)",
            "signal": "Insider net buying 3M-1Y — under 2026 1% disclosure rules, consistent insider buying is a strong conviction signal",
        })

    # Academic framework signals
    academic = {}
    # Herding: if multiple screeners hit, compute a rough herding index
    bm_hits = sum(1 for sid in [80, 92, 96, 117] if screener_hits.get(sid))
    if bm_hits >= 2:
        academic["herding_signal"] = f"High — {bm_hits}/4 big money screeners active"
        academic["herding_interpretation"] = (
            "Multiple institutional signals converging (LSV herding measure analog). "
            "When B/(B+S) deviates significantly from random, institutional herding is present."
        )
    else:
        academic["herding_signal"] = f"Low — {bm_hits}/4 big money screeners active"
        academic["herding_interpretation"] = "Limited institutional convergence detected."

    # Lead-lag: institutional buying today → retail follows 1-3 days
    if net_f > 0 and abs(pc) < 2:
        academic["lead_lag"] = "Institutional accumulation phase — VAR models suggest retail follows 1-3 days later"
    elif net_f > 0 and pc > 2:
        academic["lead_lag"] = "Retail catching up — price moving with institutional flow (lead-lag closing)"
    elif net_f < 0:
        academic["lead_lag"] = "Institutional distribution — expect retail selling 1-3 days behind"
    else:
        academic["lead_lag"] = "No clear lead-lag signal"

    # FAM (Flow-Adjusted Momentum)
    fam = pc * (1 if net_f > 0 else -1 if net_f < 0 else 0)
    academic["fam"] = round(fam, 2)
    academic["fam_interpretation"] = (
        "Positive FAM = price and flow aligned (momentum confirmed). "
        "Negative FAM = divergence (potential reversal)."
    )

    # Market structure context
    academic["market_structure"] = (
        "Institutional ownership ~93-94% of IDX equity. "
        "Avg institutional trade ~136x larger than retail. "
        "Foreign share of free-float ~70%."
    )

    return {
        "symbol": symbol,
        "name": info.get("name", ""),
        "sector": info.get("sector", ""),
        "price": info.get("price", 0),
        "market_cap": info.get("market_cap", 0),
        "bm_score": min(bm, 50),
        "value_score": min(val, 50),
        "total_score": min(bm, 50) + min(val, 50),
        "bm_breakdown": bm_breakdown,
        "val_breakdown": val_breakdown,
        "pe": stats.get("pe", 0),
        "pbv": stats.get("pbv", 0),
        "roe": stats.get("roe", 0),
        "dy": stats.get("dy", 0),
        "eps_growth": stats.get("eps_growth", 0),
        "net_foreign": flow_data["net_foreign"],
        "top_broker": broker_data["top_broker"],
        "institutional_pct": broker_data["institutional_pct"],
        "flow_signal": flow_signal,
        "performance": perf,
        "analyst": analyst,
        "broker_detail": broker_data["brokers"][:5],
        "broker7d_detail": broker7d["brokers"][:5],
        "screener_hits": {
            sid: SCREENERS[sid]["name"]
            for sid in [80, 92, 96, 117, 27, 107]
            if screener_hits.get(sid)
        },
        "unique_contributions": unique,
        "academic_framework": academic,
    }


# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/settings")
async def get_settings():
    token = get_token()
    if token:
        masked = token[:15] + "..." + token[-4:]
    else:
        masked = ""
    return {"token": masked, "has_token": bool(token)}


@app.post("/api/settings")
async def save_settings(request: Request):
    body = await request.json()
    token = body.get("token", "").strip()
    if token and not token.startswith("Bearer "):
        token = f"Bearer {token}"
    cfg = load_config()
    cfg["stockbit_token"] = token
    save_config(cfg)
    return {"ok": True}


@app.get("/api/results")
async def get_results():
    if RESULTS_PATH.exists():
        return json.loads(RESULTS_PATH.read_text())
    return {"results": [], "scan_time": None}


@app.get("/api/scan")
async def scan(request: Request):
    token = get_token()
    if not token:
        return {"error": "No Stockbit token configured. Go to Settings."}

    async def event_generator():
        try:
            async with make_session(token) as session:
                # Phase 1: Fetch all screeners
                total_steps = len(SCREENERS) + 2  # screeners + enrich + score
                step = 0

                screener_results: Dict[int, Set[str]] = {}
                all_tickers: Set[str] = set()

                for sid, screener in SCREENERS.items():
                    step += 1
                    yield {
                        "event": "progress",
                        "data": json.dumps({
                            "step": step,
                            "total": total_steps,
                            "message": f"Fetching screener: {screener['name']}...",
                            "pct": int(step / total_steps * 40),
                        }),
                    }
                    tickers = await fetch_screener(session, screener)
                    screener_results[sid] = set(tickers)
                    all_tickers.update(tickers)
                    log.info("Screener %s (%s): %d stocks",
                             sid, screener["name"], len(tickers))

                if not all_tickers:
                    yield {
                        "event": "error",
                        "data": json.dumps({"message": "No stocks found in any screener. Check your token."}),
                    }
                    return

                yield {
                    "event": "progress",
                    "data": json.dumps({
                        "step": step,
                        "total": total_steps,
                        "message": f"Found {len(all_tickers)} unique stocks. Enriching...",
                        "pct": 40,
                    }),
                }

                # Phase 2: Enrich each stock
                enriched: Dict[str, dict] = {}
                ticker_list = sorted(all_tickers)
                batch_size = 5

                for i in range(0, len(ticker_list), batch_size):
                    batch = ticker_list[i:i + batch_size]
                    tasks = [enrich_stock(session, sym) for sym in batch]
                    results = await asyncio.gather(*tasks)
                    for sym, data in zip(batch, results):
                        enriched[sym] = data
                    pct = 40 + int((i + len(batch)) / len(ticker_list) * 45)
                    yield {
                        "event": "progress",
                        "data": json.dumps({
                            "step": step + 1,
                            "total": total_steps,
                            "message": f"Enriched {min(i + batch_size, len(ticker_list))}/{len(ticker_list)} stocks...",
                            "pct": pct,
                        }),
                    }
                    await asyncio.sleep(0.3)

                # Phase 3: Score
                yield {
                    "event": "progress",
                    "data": json.dumps({
                        "step": total_steps,
                        "total": total_steps,
                        "message": "Computing scores...",
                        "pct": 90,
                    }),
                }

                scored = []
                for sym in ticker_list:
                    hits = {
                        sid: sym in tickers
                        for sid, tickers in screener_results.items()
                    }
                    result = compute_scores(sym, hits, enriched.get(sym, {}))
                    scored.append(result)

                # Sort by total score descending
                scored.sort(key=lambda x: x["total_score"], reverse=True)

                # Add rank
                for i, s in enumerate(scored):
                    s["rank"] = i + 1

                # Cache results
                output = {
                    "results": scored,
                    "scan_time": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "total_stocks": len(scored),
                }
                RESULTS_PATH.write_text(json.dumps(output, indent=2, default=str))

                yield {
                    "event": "progress",
                    "data": json.dumps({
                        "step": total_steps,
                        "total": total_steps,
                        "message": f"Done! {len(scored)} stocks scored.",
                        "pct": 100,
                    }),
                }
                yield {
                    "event": "results",
                    "data": json.dumps(output, default=str),
                }

        except Exception as e:
            log.exception("Scan error")
            yield {
                "event": "error",
                "data": json.dumps({"message": str(e)}),
            }

    return EventSourceResponse(event_generator())
