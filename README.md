# Retail Sales Analysis

## Project Overview

This project analyzes retail and warehouse sales data stored in a SQLite database. The analysis identifies sales trends by item type and month, offering actionable insights for business decision-making.

### Key Features
1. **Trend Analysis**: Sales by item type and monthly trends.
2. **Visualizations**: Saved charts for easy interpretation of data.
3. **Dynamic Reports**: Automated updates to insights and visualizations.

---

## Setup Instructions

### Prerequisites
1. **SQLite Database**: Ensure the database file `productsales.db` is accessible in the `data/` directory.
   - If you're using **DB Browser for SQLite**, you can export and place the `.db` file in this project structure.
2. **Python Environment**: Python 3.7 or above is recommended.

### Installation Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/.git
   cd 10EQS

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Confirm the database location:
   ```bash
   Place your SQLite database file productsales.db in the data/ folder.

4. Run the analysis:
   ```bash
   python src/analysis.py data/productsales.csv
