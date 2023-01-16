import dash
from dash import dcc
from dash import html
import page_cash
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    html.H1('DASHBOARD'),
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Кредиты', value='tab-cash'),
        dcc.Tab(label='Пассивы', value='tab-dep'),
        dcc.Tab(label='Кредитные карты', value='tab-cc'),
        dcc.Tab(label='Дебетовые карты', value='tab-dc'),
    ]),
    html.Div(id='tabs-content')
])


# Добавляем содержимое в зависимости от выбранной вкладки
@app.callback(Output('tabs-content', 'children'), Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-cash':
        return page_cash.html
    elif tab == 'tab-dep':
        return html.Div([
        ])
    elif tab == 'tab-cc':
        return html.Div([
        ])
    elif tab == 'tab-dc':
        return html.Div([
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
