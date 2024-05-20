from fastapi import FastAPI

from src.routers import questions, teams

app = FastAPI()


# Include routers
app.include_router(questions.router, prefix="/questions", tags=["Questions"])
app.include_router(teams.router, prefix="/teams", tags=["Teams"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Quiz App!"}
