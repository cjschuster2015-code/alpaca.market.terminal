import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient

load_dotenv()

def get_trading_client():
    client = TradingClient(
        os.getenv("ALPACA_API_KEY"),
        os.getenv("ALPACA_SECRET_KEY"),
        paper=True
    )
    return client

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, timedelta

def get_historical_bars(symbol, days=30):
    data_client = StockHistoricalDataClient(
        os.getenv("ALPACA_API_KEY"),
        os.getenv("ALPACA_SECRET_KEY")
    )

    end = datetime.now()
    start = end - timedelta(days=days)

    request_params = StockBarsRequest(
        symbol_or_symbols=symbol,
        timeframe=TimeFrame.Minute,
        start=start,
        end=end
    )

    bars = data_client.get_stock_bars(request_params)
    df = bars.df
    return df
from alpaca.data.requests import StockLatestQuoteRequest

def get_latest_quote(symbol):
    data_client = StockHistoricalDataClient(
        os.getenv("ALPACA_API_KEY"),
        os.getenv("ALPACA_SECRET_KEY")
    )
    request_params = StockLatestQuoteRequest(symbol_or_symbols=symbol)
    quote = data_client.get_stock_latest_quote(request_params)
    return quote[symbol]