# This program tests a moving average crossover strategy on NVDA, simulating trades based on the 50-day and 200-day averages and visualizing the performance.
from backtest_engine import (
    sma_crossover,
    backtest,
    sharpe_ratio,
    plot_equity,
    plot_signals,
    calculate_max_drawdown,
    calculate_cagr
)
from backtest_engine import sma_crossover, calculate_max_drawdown, calculate_cagr, backtest, sharpe_ratio, plot_equity, plot_signals
from utils import*
import pandas as pd

all_data = {}
results = {}

for ticker in ticker_list:
    all_data[ticker] = download_data(ticker)
    all_data[ticker] = sma_crossover(all_data[ticker])
    
    final_value, cumulative_returns = backtest(all_data[ticker])
    
    results[ticker] = {
        "final_value": final_value,
        "cumulative_returns": cumulative_returns,
        "sharpe": sharpe_ratio(all_data[ticker]['Strategy Returns'])

    }

    print(f"{ticker}: Final Value = ${results[ticker]['final_value']:,.2f}, Sharpe Ratio = {results[ticker]['sharpe']:.2f}")
    
    plot_equity(results[ticker]['cumulative_returns'], ticker)
    plot_signals(all_data[ticker], ticker)

portfolio_df = pd.DataFrame({
    ticker: results[ticker]['cumulative_returns']
    for ticker in results
})

portfolio_df = portfolio_df.fillna(method='ffill').fillna(method='bfill')

portfolio_values = portfolio_df.mean(axis=1)

max_dd = calculate_max_drawdown(portfolio_values)
cagr = calculate_cagr(portfolio_values)

print(f"Max Drawdown: {max_dd:.2%}")
print(f"CAGR: {cagr:.2%}")

print(all_data[ticker].columns)