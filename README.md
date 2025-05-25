#Gold Price Visualizer

This Python program reads gold price data from a CSV file and generates an interactive line graph using Plotly, showing how the price of gold has changed over time

---

## Features

- Reads historical gold price data from a CSV.
- Displays an interactive Plotly line chart.
- Gold-themed color styling.
- Clean and minimal interface.

---

## CSV Format

The CSV data file should be named `GoldHistoricalData.csv` and should contain the following columns:

| Column | Description         |
|--------|---------------------|
| Date   | Timestamps in ISO or standard date format (`YYYY-MM-DD HH:MM`) |
| Price  | Gold price in USD   |

### For Example:

"Date","Price"
"05/23/2025","3,365.80"

pip install plotly pandas

## Dependencies & Setup

Create a virtual environment: python -m venv venv
Activate the environment
### On macOS/Linux:
source venv/bin/activate
### On Windows:
.\venv\Scripts\activate

The program depends upon the pandas and plotly libraries, which can be installed with pip
Run the command:
pip install pandas plotly
or
pip install -r requirements.txt

## Usage

1. Ensure your CSV data file is named `GoldHistoricalData.csv` and placed in the same directory as `graph_stock_data.py`.
2. Run the script: python graph_stock_data.py
3. The program will open an interactive web application of your historical data in your default web browser

## License

This project is licensed under the [MIT License](LICENSE).