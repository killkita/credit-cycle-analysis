# scripts/ingest.py

import os
from dotenv import load_dotenv
from fredapi import Fred
import pandas as pd
from sqlalchemy import create_engine

# ── 1. Load your API key from the .env file ──────────────────────────────────
load_dotenv()
fred = Fred(api_key=os.getenv("FRED_API_KEY"))

# ── 2. Define the series you want to download ────────────────────────────────
SERIES = {
    "fed_funds_rate":          "FEDFUNDS",
    "commercial_loans":        "BUSLOANS",
    "consumer_credit":         "TOTALSL",
    "mortgage_rate_30yr":      "MORTGAGE30US",
    "credit_card_delinquency": "DRCCLACBS",
    "cpi":                     "CPIAUCSL",
}

# ── 3. Download each series and combine into one DataFrame ───────────────────
print("Downloading data from FRED...")

frames = []

for column_name, series_id in SERIES.items():
    print(f"  Fetching {series_id}...")
    data = fred.get_series(series_id, observation_start="1990-01-01")
    df = data.to_frame(name=column_name)
    frames.append(df)

combined = pd.concat(frames, axis=1)
combined.index.name = "date"
combined = combined.reset_index()

print(f"\nDownloaded {len(combined)} rows of data.")
print(combined.head())

# ── 4. Connect to SQLite database ────────────────────────────────────────────
engine = create_engine("sqlite:///data/fred_data.db")

# ── 5. Write to table ────────────────────────────────────────────────────────
combined.to_sql("macro_series", con=engine, if_exists="replace", index=False)

print("\n✓ Data successfully written to data/fred_data.db")
print(f"  Table: macro_series | Rows: {len(combined)}")