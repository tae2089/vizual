import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

#데이터 불러오기
df = pd.read_csv('/Users/imtaebin/Downloads/sample_test.csv',encoding = 'cp949')

#데이터 테이블 만들기
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

# css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#앱 구현
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#html 탑재하기
app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])

#앱 실행
if __name__ == '__main__':
    app.run_server(debug=True)
