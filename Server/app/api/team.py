from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.crud.team import create_team, delete_team, read_team, update_team
from app.schemas.team import Team, TeamCreate, TeamUpdate

router = APIRouter()


@router.post("/", response_model=Team)
async def create_team_endpoint(*, db: Session = Depends(get_db), team: TeamCreate):
    try:
        return create_team(db=db, team=team)

    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail=f"A team with the name {team.team_name} already exists!",
        )


@router.get("/", response_model=Team)
async def get_team_endpoint(*, db: Session = Depends(get_db), team_id: int):
    db_team = read_team(db=db, team_id=team_id)

    if not db_team:
        raise HTTPException(
            status_code=404, detail=f"A team with the id {team_id} does not exist!"
        )

    return db_team


@router.put("/", response_model=Team)
async def update_team_endpoint(
    *, db: Session = Depends(get_db), team_id: int, team: TeamUpdate
):
    db_team = read_team(db=db, team_id=team_id)

    if not db_team:
        raise HTTPException(
            status_code=404, detail=f"A team with the id {team_id} does not exist!"
        )

    return update_team(db=db, team_id=team_id, team=team)


@router.delete("/")
async def delete_team_endpoint(*, db: Session = Depends(get_db), team_id: int):
    db_team = read_team(db=db, team_id=team_id)

    if not db_team:
        raise HTTPException(
            status_code=404, detail=f"A team with the id {team_id} does not exist!"
        )

    return delete_team(db=db, team_id=team_id)
