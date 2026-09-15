from fastapi import FastAPI

app = FastAPI(root_path="/api")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello():
    return {"message": "FastAPI 연결 성공!"}