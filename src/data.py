from pathlib import Path

import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split


ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw" / "wine.csv"
TRAIN_PATH = ROOT / "data" / "processed" / "train.csv"
TEST_PATH = ROOT / "data" / "processed" / "test.csv"
RANDOM_STATE = 42

FEATURES = [
    "alcohol",
    "malic_acid",
    "color_intensity",
    "proline",
]


def ensure_raw_data() -> None:
    if RAW_PATH.exists():
        return

    RAW_PATH.parent.mkdir(parents=True, exist_ok=True)
    wine = load_wine(as_frame=True)
    wine.frame[FEATURES + ["target"]].to_csv(RAW_PATH, index=False)


def remove_outliers(df: pd.DataFrame) -> pd.DataFrame:
    mask = pd.Series(True, index=df.index)

    for column in FEATURES:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        mask &= df[column].between(q1 - 1.5 * iqr, q3 + 1.5 * iqr)

    return df.loc[mask]


def main() -> None:
    ensure_raw_data()

    df = pd.read_csv(RAW_PATH)
    df = df.drop_duplicates().dropna()
    df = remove_outliers(df)

    train, test = train_test_split(
        df,
        test_size=0.2,
        stratify=df["target"],
        random_state=RANDOM_STATE,
    )

    TRAIN_PATH.parent.mkdir(parents=True, exist_ok=True)
    train.to_csv(TRAIN_PATH, index=False)
    test.to_csv(TEST_PATH, index=False)
    print(f"wrote {len(train)} train rows and {len(test)} test rows")


if __name__ == "__main__":
    main()
