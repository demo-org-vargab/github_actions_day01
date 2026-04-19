import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc

# Initialize app with a modern Bootstrap theme
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Sample data
chart_data = pd.DataFrame({
    'x': list(range(30)),
    'y': [2 ** x for x in range(30)]
})

# Create figure with better styling
fig = px.line(
    chart_data,
    x='x',
    y='y',
    markers=True,
    template='plotly_dark',
    title="Growth Trend 📈"
)

fig.update_layout(
    title_x=0.5,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(size=14),
)

# Layout
app.layout = dbc.Container([

    # Header
    dbc.Row([
        dbc.Col(
            html.Div([
                html.H1("🚀 Hello Gargi!", className="text-center mb-2"),
                html.P("A modern interactive dashboard built with Dash",
                       className="text-center text-muted")
            ]),
            width=12
        )
    ], className="mb-4"),

    # Card for graph
    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardHeader("📊 Data Visualization"),
                dbc.CardBody([
                    dcc.Graph(
                        id='fare-scatter',
                        figure=fig,
                        config={"displayModeBar": False}
                    )
                ])
            ], className="shadow-lg border-0"),
            width=12
        )
    ]),

    # Footer
    dbc.Row([
        dbc.Col(
            html.P("Built with ❤️ using Dash & Plotly",
                   className="text-center mt-4 text-muted"),
            width=12
        )
    ])

], fluid=True, className="p-4")

if __name__ == '__main__':
    app.run(debug=True)
