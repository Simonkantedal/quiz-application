from fastapi import APIRouter, HTTPException, Depends
from models import Question
from crud import CRUD
from main import db

router = APIRouter()
crud = CRUD(db)


@router.post("/", response_model=Question)
async def create_question(question: Question):
    question_id = await crud.create_question(question)
    return {**question.dict(), "id": question_id}


@router.get("/{question_id}", response_model=Question)
async def read_question(question_id: str):
    question = await crud.get_question(question_id)
    if question:
        return question
    raise HTTPException(status_code=404, detail="Question not found")


@router.put("/{question_id}", response_model=Question)
async def update_question(question_id: str, question: Question):
    updated_question = await crud.update_question(question_id, question)
    return updated_question


@router.delete("/{question_id}")
async def delete_question(question_id: str):
    deleted = await crud.delete_question(question_id)
    if deleted:
        return {"detail": "Question deleted"}
    raise HTTPException(status_code=404, detail="Question not found")
