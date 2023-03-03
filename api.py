import uvicorn
from fastapi import FastAPI, HTTPException, status, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from models.models import BaseResponse, Quiz

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
async def getQuiz(id: str=None) -> BaseResponse:
    success, data, error = True, None, None
    try:
        data = {"quiz": core.getQuiz(id)}
    except Exception as e:
        error = str(e)
        success = False
    return BaseResponse(success, error, {"quiz": data})


@app.get("/api/getQuestions", response_model=BaseResponse)
async def getQuestions(id: str=None) -> BaseResponse:
    success, data, error = True, None, None
    try:
        data = {"questions": core.getQuestions(id)}
    except Exception as e:
        error = str(e)
        success = False
    return BaseResponse(success, error, data)


@app.get("/api/getOptions", response_model=BaseResponse)
async def getOptions(id: str=None) -> BaseResponse:
    success, data, error = True, None, None
    try:
        data = {"options": core.getOptions(id)}
    except Exception as e:
        error = str(e)
        success = False
    
    return BaseResponse(success, error, data)    


@app.put("/api/createQuiz", response_model=BaseResponse)
async def createQuiz(body: Quiz) -> BaseResponse:
    success, data, error = True, None, None
    try:
        data = {"quiz": core.upsertQuiz(body)}
    except Exception as e:
        error = str(e)
        success = False
    return BaseResponse(success, error, data)


@app.patch("/api/updateQuiz", response_model=BaseResponse)
async def updateQuiz(body: Quiz) -> BaseResponse:
    success, data, error = True, None, None
    try:
        data = {"quiz": core.upsertQuiz(body)}
    except Exception as e:
        error = str(e)
        success = False
    return BaseResponse(success, error, data)


@app.delete("api/deleteQuiz", response_model=BaseResponse)
async def deleteQuiz(id: str) -> BaseResponse:
    success, data, error = True, None, None
    try:
        data = {"quiz": core.deleteQuiz(body)}
    except Exception as e:
        error = str(e)
        success = False
    return BaseResponse(success, error, data)


@app.post("/api/submitQuiz", response_model=BaseResponse)
async def submitQuiz(body: Quiz) -> BaseResponse:
    success, data, error = True, None, None
    try:
        data = {"quiz": core.submitQuiz(body)}
    except Exception as e:
        error = str(e)
        success = False
    return BaseResponse(success, error, data)


@app.get("/api/health", response_model=BaseResponse)
async def health() -> BaseResponse:
    return BaseResponse(True, None, {"status": "healthy"})


if __name__ == "__main__":
    print("[⚙] Starting API on port {}".format(5008))
    uvicorn.run("api:app", host="0.0.0.0", port=5008)