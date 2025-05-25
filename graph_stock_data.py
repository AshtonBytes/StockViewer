import pandas as pd
import plotly.express as pex

def plot_gold_prices_from_csv(csv_path):
    data_frame = pd.read_csv(csv_path)

    data_frame['Date'] = pd.to_datetime(data_frame['Date'])
    data_frame = data_frame.sort_values('Date')

    gold_price_figure = pex.line(data_frame, x='Date', y='Price', title='Gold Price Over Time')
    gold_price_figure.update_traces(line_color='gold')
    gold_price_figure.update_layout(
        xaxis_title='Time (d)',
        yaxis_title='Price (USD)',
        template='plotly_white')
    gold_price_figure.show()

if __name__ == "__main__":
    plot_gold_prices_from_csv("GoldHistoricalData.csv")