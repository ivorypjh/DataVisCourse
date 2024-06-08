from pydantic import BaseModel

# 사용할 변수 이름과 변수 타입을 지정
class Todo(BaseModel):
	# 필수
    data_num: int
    #선택
	data_type: str | None = None