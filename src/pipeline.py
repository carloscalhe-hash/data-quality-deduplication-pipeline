import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "sample_dataset.csv"
OUTPUT_PATH = BASE_DIR / "data" / "duplicates_found.csv"


def load_data():
    return pd.read_csv(DATA_PATH)


def detect_duplicates(df, column):
    return df[df.duplicated(column, keep=False)]


def main():

    print("Loading dataset...")
    df = load_data()

    print("Checking duplicated emails...")
    dup_email = detect_duplicates(df, "email")

    print("Checking duplicated phones...")
    dup_phone = detect_duplicates(df, "phone")

    duplicates = pd.concat([dup_email, dup_phone]).drop_duplicates()

    duplicates.to_csv(OUTPUT_PATH, index=False)

    print("Done.")
    print("Duplicates saved to:", OUTPUT_PATH)


if __name__ == "__main__":
    main()
