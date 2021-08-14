from pathlib import Path
import pandas as pd
from config import config

def simulate(initial, monthly, rate, years):
    savings = initial
    rows    = list()
    for yr in range(1, years + 1):
        for _ in range(12):
            savings += monthly

        # this is an approximation since stock prices
        # are not yearly discrete and only increase on average
        savings += savings * rate
        rows.append({"year": yr, "savings": savings})
    return pd.DataFrame(rows)

def main():
    root = Path("./").absolute()
    N = len(config["initial"])
    for i in range(N):
        initial = config["initial"][i]
        rate    = config["rate"][i]
        monthly = config["monthly"][i]
        years   = config["years"][i]
        fn = f"{initial=}_{rate=}_{monthly=}_{years=}.csv"
        dst = root / fn
        simulate(initial, monthly, rate, years).to_csv(dst, index=False)

if __name__ == "__main__":
    main()
