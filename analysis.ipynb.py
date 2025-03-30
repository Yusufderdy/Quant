import matplotlib.pyplot as plt
import yfinance as yf

data = yf.download("AAPL", start="2023-01-01")
data['Close'].plot(title="Apple Aktienkurs 2023")
plt.show()