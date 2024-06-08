# 시각화를 위한 import
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio

# html로 변환해서 사용하기 위해 import
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse


# 함수 import
from vistest import make_graph
from vistest2 import make_graph2


# 라우터 객체 생성
todo_router = APIRouter()

# 데이터를 저장할 list 생성
todo_list = []

# 데이터 읽어오기
#file_path = './data/data.csv'
#data = pd.read_csv(file_path)
#print(data.head())

# todo 요청을 post 방식으로 요청한 경우 처리
@todo_router.post("/todo")
# 매개변수를 받아서 todo_list에 삽입
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo added successfully."
}

# todo 요청을 get 방식으로 요청한 경우 처리
@todo_router.get("/todo")
async def retrieve_todo() -> dict:
    return {
        "todos": todo_list
}

# 매개변수로 사용하려는 부분에 { } 와 변수 이름을 사용해서 지정
@todo_router.get("/todo/{data_type}")
async def read_data(data_type: str) -> dict:
    if data_type == 'int':
        return {
        "todo": 'success'
}
    else:
        return{
            "todo": 'type error'
        }

# 시각화 테스트
@todo_router.get("/vis/{data_num}", response_class=HTMLResponse)
async def read_data(data_num: int) -> str:
    if data_num == 1:

        # import한 함수를 활용해 데이터를 가지고 그래프를 생성한 다음
        # 그래프를 html로 변환
        graph_html = make_graph(data_num)
        graph_html_2 = make_graph2(data_num)


        # 전체 html 응답 생성
        html_content = f"""
        <html>
            <head>
                <title>Recommendation Graph</title>
            </head>
            <body>
                <h1>Data Vis for User {data_num}</h1>
                {graph_html}
                {graph_html_2}
            </body>
        </html>
        """
        return html_content

    else:
        raise HTTPException(status_code=404, detail="Invalid Data Number")
