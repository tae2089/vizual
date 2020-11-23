import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv(
    'gapminderDataFiveYear.csv')

#css적용
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#앱 생성
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    #그래프 생성
    dcc.Graph(id='graph-with-slider'),
    #슬라이더 생성
    dcc.Slider(
        #슬라이더 명
        id='year-slider',
        #데이터 프레임 year의 최솟값
        min=df['year'].min(),
        #데이터 프레임 year의 최대값
        max=df['year'].max(),
        #defalut
        value=df['year'].min(),
        #년도 mark표시하기
        marks={str(year): str(year) for year in df['year'].unique()},
        # 모르겠음
        step=None
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    #해당 연도 데이터만 뽑아네기
    filtered_df = df[df.year == selected_year]

    #그래프 생성
    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                    size="pop", color="continent", hover_name="country",
                    log_x=True, size_max=55)
    
    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
