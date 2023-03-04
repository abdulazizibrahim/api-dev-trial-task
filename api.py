import uvicorn
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware

from models.models import Answers, BaseResponse, Quiz
from src import core

app = FastAPI(
    title="Trial Task API",
    description="API task for to submit and retrieve quizes.",
    version="1.0.0",
    docs_url="/swagger",
    openapi_url="/openapi.json",
    redoc_url="/redoc",
    redoc_options={"spec_url": "/openapi.json"},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/getQuiz", response_model=BaseResponse)
async def getQuiz(response: Response, id: str=None) -> BaseResponse:
    success, data, error = True, None, None
    try:
        data = {"quiz": core.getQuiz(id)}
    except Exception as e:
        error = str(e)
        success = False
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return BaseResponse(success, error, data)


@app.put("/api/createQuiz", response_model=BaseResponse)
async def createQuiz(body: Quiz, response: Response) -> BaseResponse:
    success, data, error = True, None, None
    try:
        body = body.dict()
        data = {"quiz": core.upsertQuiz(body)}
    except Exception as e:
        error = str(e)
        success = False
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return BaseResponse(success, error, data)


@app.patch("/api/updateQuiz", response_model=BaseResponse)
async def updateQuiz(body: Quiz, response: Response) -> BaseResponse:
    success, data, error = True, None, None
    try:
        body = body.dict()
        data = {"quiz": core.upsertQuiz(body)}
    except Exception as e:
        error = str(e)
        success = False
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return BaseResponse(success, error, data)


@app.delete("/api/deleteQuiz", response_model=BaseResponse)
async def deleteQuiz(id: str, response: Response) -> BaseResponse:
    success, data, error = True, None, None
    try:
        data = {"quiz": core.deleteQuiz(id)}
    except Exception as e:
        error = str(e)
        success = False
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return BaseResponse(success, error, data)


@app.post("/api/submitQuiz", response_model=BaseResponse)
async def submitQuiz(body: Answers, response: Response) -> BaseResponse:
    success, data, error = True, None, None
    try:
        body = body.dict()
        data = {"quiz": core.checkQuiz(body)}
    except Exception as e:
        error = str(e)
        success = False
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return BaseResponse(success, error, data)


@app.get("/api/health", response_model=BaseResponse)
async def health() -> BaseResponse:
    return BaseResponse(True, None, {"status": "healthy"})


if __name__ == "__main__":
    print("[⚙] Starting API on port {}".format(5008))
    uvicorn.run("api:app", host="0.0.0.0", port=5008)