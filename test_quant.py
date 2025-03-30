import numpy as np
import pandas as pd
import yfinance as yf

# Lade Apple-Aktiendaten
data = yf.download("AAPL", start="2023-01-01")
print(data.head())

# Einfache Renditeberechnung
data['Returns'] = np.log(data['Close'] / data['Close'].shift(1))
print(data['Returns'].tail())