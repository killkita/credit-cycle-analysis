# Credit Market Response to Fed Rate Hikes (1990–2026)

**Tools:** Python · SQL · SQLite · pandas · matplotlib · seaborn · statsmodels · FRED API  
**Domain:** Macroeconomics · Fixed Income · Monetary Policy

---

## Overview

This project looks at how different credit markets respond to Federal Reserve rate hikes and whether the speed of that response has changed across historical tightening cycles.

Using 36 years of Federal Reserve data pulled via the FRED API, I built a SQLite database, conducted exploratory analysis across five hiking cycles, and applied cross-correlation analysis to measure how long each credit market takes to respond to a policy rate change.

---

## The Question

When the Fed raises rates, how quickly do different credit markets respond and did the 2022 to 2023 hiking cycle behave differently to what came before?

---

## What I Found

### Transmission lags vary significantly by credit type

Cross-correlation analysis across 36 years of monthly data revealed three distinct response speeds:

| Credit Market | Peak Lag | Correlation |
|---|---|---|
| 30-Year Mortgage Rate | 1 month | 0.295 |
| Commercial & Industrial Loans | 3 months | 0.174 |
| Total Consumer Credit | 11 months | 0.144 |

Mortgage markets reprice almost immediately because they track Treasury yields in real time. Business lending pulls back within a quarter as companies react to higher borrowing costs. Consumer credit takes nearly a full year to slow down, making households the last to feel the impact of monetary tightening.

### The 2022 to 2023 cycle was structurally different

Compared to the four prior hiking cycles, mortgage rates spiked faster and further than any previous cycle, rising 2.7 percentage points within months. Commercial loans were the only cycle to peak and then reverse mid-cycle, contracting from month 10 onwards. Consumer credit grew more aggressively than in any prior cycle, likely because pandemic era savings insulated households from the immediate impact of rising rates.

### It was also the most aggressive cycle in the dataset

At +4.92% over 17 months, the 2022 to 2023 cycle delivered the largest rate increase in the shortest timeframe since 1994, nearly 50% larger than the next biggest cycle which was 2004 to 2006 at +3.96% over 25 months.

---

## Project Structure

```
credit-cycle-analysis/
├── data/                              
├── notebooks/
│   ├── 01_verify_data.ipynb           
│   ├── 02_exploratory_analysis.ipynb  
│   ├── 03_lag_analysis.ipynb          
│   └── 04_regime_comparison.ipynb     
├── scripts/
│   └── ingest.py                      
├── requirements.txt
└── README.md
```

---

## Data Sources

All data sourced from the [Federal Reserve Economic Data (FRED)](https://fred.stlouisfed.org/) via the `fredapi` Python library:

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
git clone https://github.com/killkita/credit-cycle-analysis.git
cd credit-cycle-analysis

python3.11 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

echo "FRED_API_KEY=your_key_here" > .env

python scripts/ingest.py

jupyter notebook
```

---

## Limitations

Cross-correlation does not imply causation as other macroeconomic factors including inflation expectations, bank lending standards, and fiscal policy all influence credit markets simultaneously. FRED data is also revised retrospectively so early observations may differ from what was available in real time. Finally, five hiking cycles is a relatively small sample which limits how far the findings can be generalised.

---

## Author

**Kita** | ~ Aspiring data analyst playing with Python ~
[GitHub](https://github.com/killkita)