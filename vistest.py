import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio

def make_graph(data_num):

    file_path = './data/data.csv'

    # plotly를 사용해서 그래프 생성
    data = pd.read_csv(file_path)
    age = data['구분']
    year = data['2022_M']

    # x축과 y축에 해당하는 데이터를 각각 넣고 리스트로 감싸줌
    data = [go.Bar(x = age, y = year)]
    # 데이터 전달
    fig = go.Figure(data = data)

    fig.update_layout(title = 'Data Vis test',
    xaxis_title = 'Type',
    yaxis_title = 'Year & Sex')

    # 그래프를 html로 변환
    graph_html = pio.to_html(fig, full_html = False)

    return graph_html