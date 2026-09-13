import matplotlib.pyplot as plt
# visualized results
def plot_equity(cumulative_returns, ticker):
    cumulative_returns.plot(title=f"{ticker}'s Equity Curve")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.grid()
    plt.show()

# Buy or sell
def plot_signals(data, ticker):
    plt.figure(figsize=(14, 6))
    plt.plot(data['Close'], label='Price')
    plt.plot(data['SMA50'], label='SMA50', alpha=0.7)
    plt.plot(data['SMA200'], label='SMA200', alpha=0.7)
    plt.plot(data['SMA_Spread'], label='SMA_Spread', alpha=0.7)
    plt.plot(data['Momentum'], label='Momentum', alpha=0.7)
    plt.plot(data['Volatility'], label='Volatility', alpha=0.7)
    plt.scatter(data.index[data['Position'] == 1], data['Close'][data['Position'] == 1], label='Buy', marker='^', color='green')
    plt.scatter(data.index[data['Position'] == -1], data['Close'][data['Position'] == -1], label='Sell', marker='v', color='red')
    plt.title(f"SMA Crossover Buy/Sell Signals for {ticker}")
    plt.xlabel("Date")
    plt.ylabel(f"Stock Price ({ticker}'s Closing price)")
    plt.legend()
    plt.grid()
    plt.show()