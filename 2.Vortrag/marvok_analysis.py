import random
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

# print all columns
pd.set_option("display.max_columns", None)

# set collumns width to 100
pd.set_option("display.width", None)

def rheinmetall():
    symbol = "RHM.DE"

    ticker = yf.Ticker(symbol)

    # get stock data for this year
    start_date = "2022-11-27"
    end = "2023-11-27"
    stock_data = ticker.history(start=start_date, end=end)

    data_list = stock_data["Close"]
    stock_data_today = data_list[-1]
    print(f"stock_data_today: {stock_data_today}")


    # mean1, std1 = norm.fit(stock_data["Close"])

    mean = np.mean(stock_data["Close"])
    std = np.std(stock_data["Close"])
    print(f"mean: {mean}, std: {std}")

    # print(f"mean1: {mean1}, std1: {std1}")

    # print(stock_data)



if __name__ == "__main__":
    rheinmetall()