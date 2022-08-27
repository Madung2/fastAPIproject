from dataclasses import asdict

import uvicorn
from typing import Optional
from fastapi import FastAPI
from app.database.conn import db
from app.common.config import conf


def create_app():
    """
    앱 함수를 실행
    ;return:
    """
    c = conf() #환경변수를 불러옴
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)

    # 데이터베이스 이니셜라이즈

    # 레디스 이니셜라이즈

    # 미들웨어 정의

    # 라우터 정의

    return app


app= create_app()

if __name__== "__main__": ##실행되는 파일이 이 파일일때
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)#reload는 개발할때 true

