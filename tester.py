# My test script

from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc
import msal

dash_app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app = dash_app.server

'''
app.layout = dbc.Container([
    my_output := dcc.Markdown(children=''),
    my_text := dcc.Input(value='Type text new')
])


@app.callback(
    Output(my_output, component_property='children'),
    Input(my_text, component_property='value')
)
def update_graph(el_texto):
    return el_texto


if __name__ == '__main__':
    app.run(debug=True)
'''

#'''
app.layout = html.Div([
    html.Div(children='Hi World! How you doin?')
])

if __name__ == '__main__':
    dash_app.run_server(debug=True)
#     app.run_server(host="192.168.200.172", port="8050", debug=True, ssl_context=context)
#   dash_app.run_server(debug=True, ssl_context="adhoc")
#'''