import math
from scipy.stats import norm
from scipy.optimize import fsolve

import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

def plot_stock(symbol):
    data = yf.download(symbol, start='2022-01-01', end='2023-12-31')
    return data

def plot_stock2():

    dax_data = plot_stock('^GDAXI')  # DAX
    rheinmetall_data = plot_stock('RHM.DE')  # Rheinmetall

    # Normalisieren Sie die Daten auf eine Einheit
    dax_close = dax_data['Close'] / dax_data['Close'].max()
    rheinmetall_close = rheinmetall_data['Close'] / rheinmetall_data['Close'].max() + 0.2

    # Berechnen Sie den gleitenden Durchschnitt
    dax_sma = dax_close.rolling(window=14).mean()
    rheinmetall_sma = rheinmetall_close.rolling(window=14).mean()

    # Berechnen Sie den Standardfehler für die Fehlerbalken
    dax_ste = dax_close.rolling(window=14, center=True).std() / np.sqrt(14)
    rheinmetall_ste = rheinmetall_close.rolling(window=14, center=True).std() / np.sqrt(14)

    fig, ax1 = plt.subplots(figsize=(14,7))

    color = 'tab:blue'
    ax1.set_xlabel('Datum')
    ax1.set_ylabel('Normalisierter Schlusskurs', color=color)
    ax1.plot(dax_close.index, dax_close.values, color=color, label='DAX')
    ax1.plot(rheinmetall_close.index, rheinmetall_close.values, color='tab:orange', label='Rheinmetall')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.fill_between(dax_close.index, (dax_sma - 2*dax_ste), (dax_sma + 2*dax_ste), color='b', alpha=.1)
    ax1.fill_between(rheinmetall_close.index, (rheinmetall_sma - 2*rheinmetall_ste), (rheinmetall_sma + 2*rheinmetall_ste), color='orange', alpha=.1)

    plt.title('DAX vs Rheinmetall (Letzte 2 Jahre)')
    plt.grid(True)
    plt.legend()

    # Erstellen Sie ein zweites y-Achsenobjekt, das den gleichen x-Achsenbereich teilt
    # ax2 = ax1.twinx()
    #
    # color = 'tab:red'
    # # Wir färben die Achsen- und Linienfarben bereits oben per Hand,
    # # daher verwenden wir hier 'tab:red' sowohl für Achsen- als auch für Zeilenfarbe
    # ax2.set_ylabel('Volumen', color=color)
    # ax2.plot(dax_data.index, dax_data['Volume'].values, color=color)
    # ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.show()


# def plot normal distribution and normal density function
def plot_normal_distribution(mu, sigma):
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 1000)
    plt.plot(x, norm.pdf(x, mu, sigma), label="normal density function")
    # plot distribution function
    plt.plot(x, norm.cdf(x, mu, sigma), label="distribution function")

    x_schnitt = find_intersection(lambda x: norm.cdf(x, mu, sigma), lambda x: norm.pdf(x, mu, sigma), 0)
    plt.plot(x_schnitt, norm.pdf(x_schnitt, mu, sigma), "ro", label=f"Schnitt bei x={x_schnitt}, y={norm.pdf(x_schnitt, mu, sigma)}")

    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

def find_intersection(func1, func2, x_guess):
    return fsolve(lambda x : func1(x) - func2(x), x_guess)


def binomial(n, t, p):
    return round(math.comb(n, t) * p ** n * (1 - p) ** (t - n), 4)


if __name__ == "__main__":
    # plot_normal_distribution(0, 0.7999)
    #r = find_intersection(lambda x: norm.cdf(x, 0, 1), lambda x: norm.pdf(x, 0, 1), 0)
    #print(r)

    plot_stock2()
