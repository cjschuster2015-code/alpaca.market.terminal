import tkinter as tk
import threading
from streamer import start_quote_stream
from data_connector import get_latest_quote

window = tk.Tk()
window.title("Mini Market Data Terminal")
window.geometry("400x300")

ticker_label = tk.Label(window, text="Enter Ticker:")
ticker_label.pack(pady=5)

ticker_entry = tk.Entry(window)
ticker_entry.pack(pady=5)

bid_label = tk.Label(window, text="Bid: --")
bid_label.pack(pady=5)

ask_label = tk.Label(window, text="Ask: --")
ask_label.pack(pady=5)

def update_labels(data):
    bid_label.config(text=f"Bid: {data.bid_price}")
    ask_label.config(text=f"Ask: {data.ask_price}")

def start_streaming():
    symbol = ticker_entry.get().upper()

    latest = get_latest_quote(symbol)
    update_labels(latest)

    thread = threading.Thread(target=start_quote_stream, args=(symbol, update_labels), daemon=True)
    thread.start()

start_button = tk.Button(window, text="Start", command=start_streaming)
start_button.pack(pady=5)

window.mainloop()