# simulate trade
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def backtest(data, initial_capital=10000):
    data['Returns'] = data['Close'].pct_change() # put the percent change over each date at close into the column 'Returns'
    data['Strategy Returns'] = data['Returns'] * data['Signal'].shift(1) # signals meaning (1 - buy, 0 - hold, -1 sell). Understanding if the strategy is profitable or not.
    cumulative_returns = initial_capital * (1 + data['Strategy Returns']).cumprod()
    final_value = cumulative_returns.iloc[-1]

    return final_value, cumulative_returns

def train_ml_model(data):
    features = ['SMA_Spread', 'Momentum', 'Volatility']
    X = data[features]
    y = data['Target']
    X_train, X_test,y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=False)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"ML Model Accuracy: {acc:.2f}")

    data.loc[X_test.index, 'ML_Pred'] = preds
    return data, model