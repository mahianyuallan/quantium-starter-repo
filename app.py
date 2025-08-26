import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load the formatted data
df = pd.read_csv("formatted_sales.csv")

# Make sure date is in datetime format
df["date"] = pd.to_datetime(df["date"])

# Aggregate sales by date
df_grouped = df.groupby("date", as_index=False)["sales"].sum()

# Create line chart
fig = px.line(
    df_grouped,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Total Sales"},
)

# Build Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center"}),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)

