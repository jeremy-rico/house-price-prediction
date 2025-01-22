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
    # print(df_train.index)
    # print(df_train.dtypes)
    print(df_train.head())
    # print(df_train.columns)
    cols = df_train.columns

    for col in cols:
        print(f"{col}: {df_train[col].dtypes}")


if __name__ == "__main__":
    main()
