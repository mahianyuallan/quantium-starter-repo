import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load the formatted data
df = pd.read_csv("formatted_sales.csv")
df["date"] = pd.to_datetime(df["date"])

# Initialise the Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div(
    style={
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": "#f9f9f9",
        "padding": "20px"
    },
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            style={"textAlign": "center", "color": "#b30059"}
        ),

        html.Div([
            html.Label("Select Region:", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="region-filter",
                options=[
                    {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                ],
                value="all",   # default selection
                inline=True,
                style={"margin": "10px 0"}
            )
        ], style={"textAlign": "center"}),

        dcc.Graph(id="sales-line-chart")
    ]
)

# Callback to update the chart
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):
    # Filter data by region if not 'all'
    if region != "all":
        filtered_df = df[df["region"] == region]
    else:
        filtered_df = df

    # Aggregate sales by date
    df_grouped = filtered_df.groupby("date", as_index=False)["sales"].sum()

    # Create line chart
    fig = px.line(
        df_grouped,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales Over Time ({region.capitalize() if region != 'all' else 'All Regions'})",
        labels={"date": "Date", "sales": "Total Sales"},
    )
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f9f9f9",
        font=dict(color="#333"),
        title_x=0.5
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
