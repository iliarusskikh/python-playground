import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1('My Dashboard'),
        dcc.Graph(
            id='My-Graph',
            figure={
                'data': [  # Changed 'Data' to 'data'
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Bar chart'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': 'Line chart'},
                ],
                'layout': {  # Ensure 'layout' is lowercase
                    'title': {'text': 'Graph title'},  # Modern Plotly expects 'text' for title
                    'xaxis': {'title': 'x-axis'},
                    'yaxis': {'title': 'y-axis'}
                }
            }
        )
    ]
)

if __name__ == '__main__':  # Fixed spacing for clarity
    app.run_server(debug=True)
