# Credit Market Response to Fed Rate Hikes (1990–2026)

**Tools:** Python · SQL · SQLite · pandas · matplotlib · seaborn · statsmodels · FRED API  
**Domain:** Macroeconomics · Fixed Income · Monetary Policy

---

## Project Overview

This project investigates how different credit markets respond to Federal Reserve interest 
rate hikes, and whether the speed and severity of that response has changed across cycles.

Using 36 years of Federal Reserve data (1990–2026), I built a SQLite database from the 
FRED API, conducted exploratory analysis across five hiking cycles, and applied 
cross-correlation analysis to quantify the transmission lag between policy rate changes 
and credit market responses.

---

## The Core Question

**When the Fed raises rates, how quickly do different credit markets respond — 
and did the 2022–23 hiking cycle behave differently to historical precedent?**

---

## Key Findings

### 1. Transmission Lags Vary Significantly by Credit Type
Cross-correlation analysis across 36 years of monthly data revealed three distinct 
response speeds:

| Credit Market | Peak Lag | Correlation |
|---|---|---|
| 30-Year Mortgage Rate | 1 month | 0.295 |
| Commercial & Industrial Loans | 3 months | 0.174 |
| Total Consumer Credit | 11 months | 0.144 |

Mortgage markets reprice almost immediately as they track Treasury yields in real time. 
Business lending contracts within a quarter as companies respond to higher borrowing costs. 
Consumer credit takes nearly a full year to slow — households are the last to feel the 
impact of monetary tightening.

### 2. The 2022–23 Cycle Was Structurally Different
Compared to the four prior hiking cycles (1994–95, 1999–00, 2004–06, 2015–18):

- **Mortgage rates** spiked +2.7pp within months — faster and larger than any prior cycle
- **Commercial loans** peaked at month 10 and reversed — the only cycle to show a clear 
  contraction within the cycle window
- **Consumer credit** grew more aggressively than any prior cycle, suggesting pandemic-era 
  savings insulated households from the immediate impact of rate rises

### 3. The 2022–23 Cycle Was the Most Aggressive in the Dataset
At +4.92% over 17 months, it delivered the largest rate increase in the shortest timeframe 
of any cycle since 1994 — nearly 50% larger than the next biggest (2004–06: +3.96% 
over 25 months).

---

## Project Structure

```
credit-cycle-analysis/
├── data/                              # SQLite database and saved charts
├── notebooks/
│   ├── 01_verify_data.ipynb           # SQL verification queries
│   ├── 02_exploratory_analysis.ipynb  # Time series visualisation
│   ├── 03_lag_analysis.ipynb          # Cross-correlation analysis
│   └── 04_regime_comparison.ipynb     # Hiking cycle comparison
├── scripts/
│   └── ingest.py                      # FRED API data pipeline
├── requirements.txt
└── README.md
```

---

## Data Sources

All data sourced from the [Federal Reserve Economic Data (FRED)](https://fred.stlouisfed.org/) 
via the `fredapi` Python library:

| Series ID | Description |
|---|---|
| FEDFUNDS | Federal Funds Effective Rate |
| BUSLOANS | Commercial & Industrial Loans |
| TOTALSL | Total Consumer Credit |
| MORTGAGE30US | 30-Year Fixed Mortgage Rate |
| DRCCLACBS | Credit Card Delinquency Rate |
| CPIAUCSL | Consumer Price Index |

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/killkita/credit-cycle-analysis.git
cd credit-cycle-analysis

# Create and activate virtual environment
python3.11 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add your FRED API key to a .env file
echo "FRED_API_KEY=your_key_here" > .env

# Run the data pipeline
python scripts/ingest.py

# Open notebooks in order
jupyter notebook
```

---

## Limitations

- Cross-correlation does not imply causation — other macroeconomic factors 
  (inflation expectations, bank lending standards, fiscal policy) influence credit markets simultaneously
- FRED data is revised retrospectively, so early observations may differ from real-time data
- The sample covers five hiking cycles which limits statistical generalisation

---

## Author

**kita** | Data Analyst  
[GitHub](https://github.com/killkita)