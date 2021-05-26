import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
    #제목
    html.H6("Change the value in the text box to see callbacks in action!"),
    #요소 추가하기
    html.Div(["Input: ",dcc.Input(id='my-input', value='initial value', type='text')]),
    #한칸 띄우기
    html.Br(),
    #Allowed arguments: accessKey, aria-*, children, className, contentEditable, contextMenu, data-*, dir, draggable, hidden, id, key, lang, loading_state, n_clicks, n_clicks_timestamp, role, spellCheck, style, tabIndex, title
    html.Div(id='my-output')
    ],style={'width': '48%', 'display': 'inline-block'}),
html.Div([
    #제목
    html.H6("Change the value in the text box to see callbacks in action!"),
    #요소 추가하기
    html.Div(["Input: ",dcc.Input(id='my-input1', value='initial value', type='text')]),
    #한칸 띄우기
    html.Br(),
    #Allowed arguments: accessKey, aria-*, children, className, contentEditable, contextMenu, data-*, dir, draggable, hidden, id, key, lang, loading_state, n_clicks, n_clicks_timestamp, role, spellCheck, style, tabIndex, title
    html.Div(id='my-output1')
    ],style={'width': '48%', 'display': 'inline-block'})
])


@app.callback(
    # my -output과 연결되어 있음
    #my-output이라는 이름에 div에 children오소로 넣어준다.
    Output(component_id='my-output', component_property='children'),
    #input은 리스트 혹은 튜플로 주어야 함,myinput과 연결되어 있음
    [Input(component_id='my-input', component_property='value')]
)
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
