import os
from dotenv import load_dotenv
from alpaca.data.live import StockDataStream

load_dotenv()

def start_quote_stream(symbol, on_quote):
    stream = StockDataStream(
        os.getenv("ALPACA_API_KEY"),
        os.getenv("ALPACA_SECRET_KEY")
    )

    async def quote_handler(data):
        on_quote(data)

    stream.subscribe_quotes(quote_handler, symbol)
    stream.run()