from fastapi import APIRouter, HTTPException, Depends

from src.crud import CRUD
from src.database import db
from src.models import Team

router = APIRouter()
crud = CRUD(db)


@router.post("/", response_model=Team)
async def create_team(team: Team):
    team_id = await crud.create_team(team)
    return {**team.dict(), "id": team_id}


@router.get("/{team_id}", response_model=Team)
async def read_team(team_id: str):
    team = await crud.get_team(team_id)
    if team:
        return team
    raise HTTPException(status_code=404, detail="Team not found")


@router.put("/{team_id}", response_model=Team)
async def update_team(team_id: str, team: Team):
    updated_team = await crud.update_team(team_id, team)
    return updated_team


@router.delete("/{team_id}")
async def delete_team(team_id: str):
    deleted = await crud.delete_team(team_id)
    if deleted:
        return {"detail": "Team deleted"}
    raise HTTPException(status_code=404, detail="Team not found")
