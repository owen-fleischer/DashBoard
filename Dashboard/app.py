# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
#df_sep = pd.read_csv.gapminder().query("country == 'Canada'")

# Initialize the app
app = Dash(__name__)

colors = {
    'background': '#111111',
    'header': '#7FDBFF'
}

# App layout
app.layout = html.Div(style={'backgroundColor': colors['background']}, children =[
    html.H1(children='Country Information', style={'textAlign' : 'center', 'color': colors['header']}),
    
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item', style={'color':colors['header']}),
    dash_table.DataTable(data=df.to_dict('records'), page_size=6, style_cell = {'backgroundColor':colors['background']}, style_data = {'color': colors['header']}),
    dcc.Graph(figure={}, id='controls-and-graph'),
    #dcc.Graph(px.bar(df_sep, x = ''))
])

# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)