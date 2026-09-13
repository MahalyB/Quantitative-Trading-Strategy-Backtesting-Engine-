# set up moving average logic
def sma_crossover(data, short_window=50, long_window=200):
    data['SMA50'] = data['Close'].rolling(window=short_window).mean()
    data['SMA200'] = data['Close'].rolling(window=long_window).mean()

    # Intialize Signal column with 0s
    data['Signal'] = 0

    # Use .loc to assign where SMA50 > SMA200 for long
    data.loc[data['SMA50'] > data['SMA200'], 'Signal'] = 1

    # shorting SMA50 < SMA200
    data.loc[data['SMA50'] < data['SMA200'], 'Signal'] = -1

    # Create Position columm to track when Signal changes (buy/sell/hold)
    data['Position'] = data['Signal'].diff()
    return data
    
def generate_features(data):
    data['Return'] = data['Close'].pct_change()

    # Moving averages
    data['SMA50'] = data['Close'].rolling(50).mean()
    data['SMA200'] = data['Close'].rolling(200).mean()

    # Spread between averages
    data['SMA_Spread'] = data['SMA50'] - data['SMA200']

    # Momentum and volatility
    data['Momentum'] = data['Close'].pct_change(10)
    data['Volatility'] = data['Return'].rolling(20).std()

    # ML label
    data['Target'] = (data['Close'].shift(-1) > data['Close']).astype(int)

    data.dropna(inplace=True)
    return data


def generate_signals(data):
    data['Signal'] = 0
    data.loc[data['SMA50'] > data['SMA200'], 'Signal'] = 1
    data.loc[data['SMA50'] < data['SMA200'], 'Signal'] = -1

    # Only trade when ML agrees (optional thresholding can be added)
    data['Final_Signal'] = 0
    data.loc[(data['Signal'] == 1) & (data['ML_Pred'] == 1), 'Final_Signal'] = 1
    data.loc[(data['Signal'] == -1) & (data['ML_Pred'] == 0), 'Final_Signal'] = -1

    return data
