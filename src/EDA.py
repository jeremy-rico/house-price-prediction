from pathlib import Path

import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt


def main():
    # Data loading
    data_path = Path("./data")
    fig_dir = data_path / "figs"

    df_train = pd.read_csv(data_path / "train.csv")

    # Data overview
    print(df_train.head())
    print(df_train.columns)


if __name__ == "__main__":
    main()
