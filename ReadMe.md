# Banking Transaction Analytics Platform

## Overview
A comprehensive analytics platform that processes banking transaction data and generates actionable business insights through multiple analytical lenses.

## Project Description
This platform demonstrates data analytics and visualization capabilities by analyzing banking transactions to uncover spending patterns, transaction trends, and account performance metrics. Includes both backend analysis and interactive Flask web dashboard.

## Features
✅ **Spending Pattern Analysis** - Identify high-value customers and spending trends  
✅ **Transaction Volume Analytics** - Breakdown of transaction types (NEFT, RTGS, IMPS)  
✅ **Account-Level Metrics** - Success rates, transaction counts, total values  
✅ **Multi-Format Export** - CSV and JSON outputs for integration  
✅ **Interactive Dashboard** - Flask-based web interface  
✅ **Error Handling & Logging** - Production-ready error management  

## Technical Stack
- **Language:** Python 3
- **Libraries:** Pandas, Flask, Logging
- **Output Formats:** CSV, JSON, HTML Dashboard
- **Visualization:** Interactive web dashboard

## Installation

```bash
pip install pandas flask
```

## Usage

### Analytics Engine
```bash
python analytics_platform.py
```

### Flask Dashboard
```bash
python flask_app.py
# Visit http://localhost:5000/
```

## Outputs
- `spending_patterns.csv` & `.json`
- `transaction_volume.csv` & `.json`
- `account_metrics.csv` & `.json`
- Interactive Flask dashboard

## Key Insights
- Identifies top spending accounts
- Analyzes transaction type distribution
- Calculates success rates per account
- Provides executive-level metrics

## Future Enhancements
- Real-time data streaming
- Advanced visualizations (charts, graphs)
- AWS S3 integration
- Email report automation