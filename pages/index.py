import dash

from home import layout

dash.register_page(__name__, path='/', redirect_from=['/index'])
