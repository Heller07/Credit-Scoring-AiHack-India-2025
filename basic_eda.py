import pandas as pd


def main():
    df = pd.read_csv("train.csv")
    print("columns:")
    print(df.columns.tolist())

    print("\ninfo:")
    df.info()

    print("\nnumeric describe:")
    print(df.describe())

    print("\nobject describe:")
    print(df.describe(include="object"))

    target = "Default 12 Flag"
    print("\ntarget counts:")
    print(df[target].value_counts())

    print("\ntarget ratio:")
    print(df[target].value_counts(normalize=True))


if __name__ == "__main__":
    main()

