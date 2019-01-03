import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc 
import dash_html_components as html 
from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.Dash()

app.layout = html.Div([
    html.H1('My Favorite Stocks'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'AMD', 'value':'AMD'},
            {'label': 'Intel', 'value':'INTC'},
            {'label': 'Nvidia', 'value':'NVDA'}
        ],
        value='AMD'
    ),
    dcc.Graph('my-graph')
]
)

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_val):
    #print(f'Updating with {selected_dropdown_val} really')
    #print(f'Updating with really')
    print("Stock selected:" + selected_dropdown_val)

    df= web.DataReader(
        selected_dropdown_val, data_source='robinhood'
        #start=dt(2018,7,1,), end=dt.now()
    )
    print(df.head(10))
    return {
        'data': [{
            'x': df.begins_at,
            'y': df.close_price
        }]
    }


if __name__ == '__main__':
    print('Starting Stock Dashboard')
    app.run_server()