
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

#data만들기
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas","Apples"],
    "Amount": [4, 1, 2, 2, 4, 5, 2],
    "City": ["SF", "SF", "SF", "seoul","seoul", "Montreal", "Montreal"]
})

#bar만들기 x는 과일, y는 총 , 색깔은 도시에 따라 바꿔주기
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

#html요소에 넣기
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': "blue"
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])





if __name__ == '__main__':
    app.run_server(debug=True)
