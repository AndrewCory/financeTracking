from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd


sample = pd.read_csv("sample.csv")

app = Dash()

direction_dropdown = dcc.Dropdown(options=sample['direction'].unique(), value='out')

app.layout = html.Div(children=[html.H1(children='Money Flow Dashboard'), direction_dropdown, dcc.Graph(id='flow-graph')])

@app.callback(
    Output(component_id='flow-graph', component_property='figure'),
    Input(component_id=direction_dropdown, component_property='value')
)
def update_graph(selected_direction):
    filtered_sample = sample[sample['direction'] == selected_direction]
    line_fig = px.bar(filtered_sample,
                       x='date', y='amount',
                       color='category',
                       title=f'money {selected_direction} over time')
    return line_fig

if __name__ == '__main__':
    app.run_server(host='127.0.0.2', port=8050, debug=True)