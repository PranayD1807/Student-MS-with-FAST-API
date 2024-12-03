from fastapi import FastAPI
from server.routes.student import router as StudentRouter

app = FastAPI()
app.include_router(StudentRouter, tags=["Student"], prefix="/api/students")


@app.get("/", tags=["root"])
async def read_root():
    return {"status": "success", "message": "Server is running!"}
