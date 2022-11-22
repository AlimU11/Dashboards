import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.icons.FONT_AWESOME, dbc.themes.BOOTSTRAP])

app.layout = dash.page_container

if __name__ == '__main__':
    app.run_server(debug=True)
