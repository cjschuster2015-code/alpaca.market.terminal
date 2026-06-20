import matplotlib.pyplot as plt
from data_connector import get_historical_bars

def plot_historical_bars(symbol, days=30):
    df = get_historical_bars(symbol, days=days)

    df = df.reset_index()

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    axes[0].plot(df["timestamp"], df["close"], label="Close Price", color="blue")
    axes[0].set_ylabel("Price ($)")
    axes[0].set_title(f"{symbol} - Last {days} Days")
    axes[0].legend()

    axes[1].bar(df["timestamp"], df["volume"], color="gray")
    axes[1].set_ylabel("Volume")
    axes[1].set_xlabel("Time")

    plt.tight_layout()
    plt.show()