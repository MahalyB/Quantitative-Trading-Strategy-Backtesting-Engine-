import numpy as np
import pandas as pd

# sharpe ratio. Calculate the amount of risk
def sharpe_ratio(returns,risk_free_rate=0.0):
    excess = returns - risk_free_rate / 252
    return np.mean(excess) / np.std(excess) * np.sqrt(252)

# max drawdown
def calculate_max_drawdown(equity_curve: pd.Series) -> float:
    """
    Calculates the maximum drawdown of a portfolio.
    """
    cumulative_max = equity_curve.cummax()
    drawdown = (equity_curve - cumulative_max) / cumulative_max
    max_drawdown = drawdown.min()
    return max_drawdown

def calculate_cagr(equity_curve: pd.Series, periods_per_year=252) -> float:
    """
    Calculates the Compound Annual Growth Rate.
    """
    total_return = equity_curve.iloc[-1] / equity_curve.iloc[0]
    years = len(equity_curve) / periods_per_year
    cagr = total_return ** (1 / years) - 1
    return cagr
