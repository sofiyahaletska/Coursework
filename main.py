import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import date
import form_request
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
# plotly.tools.set_config_file(plotly_domain='http://127.0.0.1:5000/',world_readable=False,
#                              sharing='secret')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app1 = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def draw(input_type_of_chart, input_info, input_currency):
    v1 = form_request.DefAction(input_info, input_currency, date.today())
    info = v1.form_request()
    if input_type_of_chart == "graph":
        if len(info) == 2:
            pass
        elif len(info) == 3:
            data = [go.Scatter(x=info[0], y=info[1])]
            return py.plot(data, filename='basic-line',  auto_open= True)
        else:
            raise ValueError

    else:
        if len(info) == 2:
            pass
        elif len(info) == 3:
            data = []
            for i in range(len(info[0])):
                value = info[1][i]
                name = info[0][i]
                data.append({'x': [0.5], 'y': [value], 'type': 'bar', 'name': name.strftime("%d.%m.%Y")},)
            app1.layout = html.Div(children=[
                dcc.Graph(
                    id='example-graph',
                    figure={
                        'data': data,
                        'layout': {
                            'title': info[2]
                        }
                    }
                )
            ])
        else:
            raise ValueError

    if input_type_of_chart== "chart":
        app1.run_server(debug=True)