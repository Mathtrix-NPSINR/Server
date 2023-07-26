from fastapi import APIRouter, Depends, HTTPException, Security
from loguru import logger
from sqlalchemy.orm import Session

from app.core.api_key import get_api_key
from app.core.db import get_db
from app.crud.team import create_team, delete_team, read_team, update_team
from app.schemas.team import Team, TeamCreate, TeamUpdate

router = APIRouter()


@router.post("/", response_model=Team)
async def create_team_endpoint(
        *,
        db: Session = Depends(get_db),
        api_key=Security(get_api_key),
        team: TeamCreate,
):
    db_team = create_team(db=db, team=team)
    logger.info(f"{api_key.user} created a new team with the team id {db_team.id}")
    return db_team


@router.get("/", response_model=Team)
async def get_team_endpoint(
        *, db: Session = Depends(get_db), api_key=Security(get_api_key), team_id: int
):
    db_team = read_team(db=db, team_id=team_id)

    if not db_team:
        raise HTTPException(
            status_code=404, detail=f"A team with the id {team_id} does not exist!"
        )

    logger.info(f"{api_key.user} read the details of the team id {db_team.id}")

    return db_team


@router.put("/", response_model=Team)
async def update_team_endpoint(
        *,
        db: Session = Depends(get_db),
        api_key=Security(get_api_key),
        team_id: int,
        team: TeamUpdate,
):
    db_team = read_team(db=db, team_id=team_id)

    if not db_team:
        raise HTTPException(
            status_code=404, detail=f"A team with the id {team_id} does not exist!"
        )

    logger.info(f"{api_key.user} updated the details of the team id {db_team.id}")

    return update_team(db=db, team_id=team_id, team=team)


@router.delete("/")
async def delete_team_endpoint(
        *, db: Session = Depends(get_db), api_key=Security(get_api_key), team_id: int
):
    db_team = read_team(db=db, team_id=team_id)

    if not db_team:
        raise HTTPException(
            status_code=404, detail=f"A team with the id {team_id} does not exist!"
        )

    logger.info(f"{api_key.user} deleted the team id {db_team.id}")

    return delete_team(db=db, team_id=team_id)
