import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('gdp-life-exp-2007.csv')

#x,y축 size는 인국수, color는 6대륙 hover_name = 나라 이름 넣어줌
fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                size="population", color="continent", hover_name="country",
                log_x=True, size_max=60)

# layout설정하기 html.Div를 통해 html에 div요소로 값 넣기
app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
