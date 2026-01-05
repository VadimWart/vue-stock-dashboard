import yfinance as yf
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# CORS-Einstellungen (WICHTIG für die Verbindung)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CompanyMetric(BaseModel):
    name: str
    revenue: str
    changeValue: str
    changePercent: str
    isPositive: bool
    symbol: str
    logoUrl: str
    history: List[float]


# die Top 10 und ihre Domains global
TOP_10_MAP = {
    "AAPL": "apple.com",
    "MSFT": "microsoft.com",
    "GOOGL": "google.com",
    "AMZN": "amazon.com",
    "NVDA": "nvidia.com",
    "META": "meta.com",
    "TSLA": "tesla.com",
    "BRK-B": "berkshirehathaway.com",
    "LLY": "lilly.com",
    "AVGO": "broadcom.com",
}


@app.get("/api/metrics", response_model=List[CompanyMetric])
async def get_metrics():
    results = []
    # Ticker aus Mapping
    tickers = list(TOP_10_MAP.keys())

    # Download der Kursdaten (Bulk-Download für alle 10 auf einmal ist schneller)
    data = yf.download(tickers, period="10d", interval="1d", group_by="ticker")

    for symbol in tickers:
        try:
            ticker_data = data[symbol]
            if len(ticker_data) < 2:
                continue

            history_list = ticker_data["Close"].dropna().tolist()

            current_price = ticker_data["Close"].iloc[-1]
            prev_close = ticker_data["Close"].iloc[-2]
            change_val = current_price - prev_close
            change_pct = (change_val / prev_close) * 100

            # Logo-URL über Clearbit generieren
            domain = TOP_10_MAP.get(symbol)
            logo_url = f"https://www.google.com/s2/favicons?domain={domain}&sz=128"

            results.append(
                {
                    "name": symbol,
                    "symbol": symbol,
                    "revenue": f"{current_price:.2f}",
                    "changeValue": f"{abs(change_val):.2f}",
                    "changePercent": f"{change_pct:.2f}",
                    "isPositive": change_val >= 0,
                    "logoUrl": logo_url,
                    "history": [round(p, 2) for p in history_list],
                }
            )
        except Exception as exception:
            print(f"Error processing {symbol}: {exception}")
            continue

    return results
