import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew
import yfinance as yf
import pandas as pd


def pullStockData(symbol, start_date, end_date):
    pd.set_option("display.max_columns", None) # print all columns
    pd.set_option("display.width", None) # set collumns width to 100
    ticker = yf.Ticker(symbol)
    stock_data = ticker.history(start=start_date, end=end_date)
    data_list = stock_data["Close"]
    prices = []
    for i in range(len(data_list)):
        prices.append(data_list[i])

    return prices


def markovAnalysis(prices, simDauer, anzahlSims, symbol):
    pricesX = []
    mean = np.mean(prices)
    std = np.std(prices)
    for t in range(len(prices)):
        pricesX.append(t)

    x = [len(prices)]
    y = []
    for n in range(anzahlSims):
        y.append([prices[len(prices) - 1]])

    for t in range(simDauer):
        x.append(t + 1 + len(prices))
        for n in range(anzahlSims):
            Zufallszahl = np.random.normal()
            r = np.exp(Zufallszahl * std / mean * np.sqrt(1.0 / len(prices)))
            y[n].append(y[n][t] * r)

    plt.subplot(2, 1, 1)
    plt.plot(pricesX, prices)
    for n in range(anzahlSims):
        plt.plot(x, y[n])

    plt.title(symbol + '  Markov Chain')
    plt.legend()
    plt.grid()
    plt.xlabel("Zeit in Tagen")
    plt.ylabel("Preis in €")

    plt.subplot(2, 1, 2)
    distributions = []
    for i in range(anzahlSims):
        distributions.append(y[i][100])
    plt.hist(distributions, bins=30, density=True, alpha=0.7, color='skyblue', edgecolor='black')

    plt.title('Product Distribution, skew = ' + str(int(1000 * skew(distributions)) / 1000.0), fontsize=16,
              fontweight='bold')
    plt.xlabel('Value', fontsize=12)
    plt.ylabel('Probability Density', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.gca().set_facecolor('#f5f5f5')
    plt.gca().patch.set_alpha(0.1)

    # Adjust layout to prevent overlapping
    plt.tight_layout()

    # Show the plot
    plt.show()


symbol = "RHM.DE"
# symbol = "AAPL"
prices = pullStockData(symbol, "2022-11-27", "2023-11-27")
markovAnalysis(prices, 100, 500, symbol)
