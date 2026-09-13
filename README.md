# Quantitative Trading Strategy Backtesting Engine

A Python-based backtesting project for evaluating moving-average trading strategies across U.S. equities. The project combines a traditional 50-day/200-day simple moving average (SMA) crossover strategy with a Random Forest classifier that uses engineered market features to predict next-day price direction and filter trading signals.

The backtesting engine calculates portfolio returns and evaluates strategy performance using metrics including Sharpe ratio, maximum drawdown, CAGR, and machine-learning model accuracy.

## Features

- Download historical equity data using 'yfinance'
- Calculate 50-day and 200-day simple moving averages
- Generate trading signals from SMA crossovers
- Engineer momentum, volatility, and moving-average spread features
- Train a Random Forest classifier to predict next-day price direction
- Use machine-learning predictions to filter trading signals
- Simulate strategy returns and portfolio growth
- Calculate performance metrics including:
    - Sharpe ratio
    - Maximum drawdown
    - CAGR
    - Model accuracy
- Visualize equity curves, market features, and buy/sell signals

## Supported Equities

The project can be used to evaluate:

- AAPL
- AMD
- AMZN
- GOOGL
- INTC
- META
- MSFT
- NVDA
- QCOM
- TSLA

## How It Works

### 1. Data Collection

Historial stock-price data is downloaded using 'yfinance'.

### 2. Feature Engineering

The project calculates several features from historical price data:

- 50-day simple moving average
- 200-day simple moving average
- Moving-average spread
- 10-day momentum
- 20-day volatility

### 3. Machine learning

A 'RandomForestClassifier' is trained using moving-average spread, momentum, and volatility as features. The target represents whether the following trading day's price movement is positive or negative. 

The dataset is split chronologically rather than randomly to preserve the time ordering of the financial data.

### 4. Trading Signals

The base strategy generates signals using the relationship between the 50-day and 200-day moving averages.
Predictions from the Random Forest model are then incorporated into the signal-generation process.

### 5. Backtesting

The backtesting engine calculates daily market returns and applies the strategy's previous trading signal to calculate strategy returns.

Portfolio growth is simulated from an initial capital amount.

### 6. Evaluation

Strategy performance is evaluateed using:

- Sharpe ratio
- Maximum drawdown
- Compound annual growth rate (CAGR)
- Random Forest classification accuracy
- Equity-curve visualization

## Technologies

- Python
- Pandas
- NumPy
- scikit-learn
- Matplotlib
- yfinance

## Getting Started

### Prerequisites

- Pythin 3.7+
- Dependencies listed in 'requirements.txt'

### Installation

Clone the repository:

'''bash
git clone https://github.com/MahalyB/backtest_project.git
cd backtest_project
'''

Create a virtual environment (optional but recommended):

'''bash
python3 -m venv .venv
'''

Activate the virtual environment:
**macOS/Linux:**

'''bash
source .venv/bin/activate
'''

**Windows:**

'''bash
.venv\Scripts\activate
'''

Install the required dependencies:

'''bash
pip install -r requirements.txt
'''

## Usage

Run the backtesting progam:

'''bash
python backtest.py
'''

The program will:

- Download historical stock data 
- Calculate moving-average and market features
- Train the Random Forest classifier
- Generate trading signals
- Run the backtest
- Calculate strategy performance metrics
- Display strategy visualizations

## Project Purpose

I built this project to learn how quantitative trading strategies can be implemented and evaluated using Python. Through the project, I gained experience working with financial time-series data, feature engineering, machine learning, modular Python development, and quantitative performance metrics.

## Future Improvements

- Implement walk-forward validation for the machine-learning model
- Add additional trading strategies and technical indicators
- Compare strategy performance against a buy-and-hold benchmark
- Add transaction costs and slippage to the backtesting engine
- Expand strategy testing across additional securities and time periods

## Disclaimer

This projet is for educational purposes only and is not intended to provide financial or investment advice.
