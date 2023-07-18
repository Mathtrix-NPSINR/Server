from sqlalchemy.orm import Session

import app.models.team as team_models
import app.schemas.team as team_schemas


def create_team(db: Session, team: team_schemas.TeamCreate):
    db_team = team_models.Team(
        team_school=team.team_school,
        team_event=team.team_event,
        event_id=team.event_id,
    )

    db.add(db_team)
    db.commit()
    db.refresh(db_team)

    return db_team


def read_team(db: Session, team_id: int):
    db_team = db.query(team_models.Team).filter(team_models.Team.id == team_id).first()

    return db_team


def update_team(db: Session, team_id: int, team: team_schemas.TeamUpdate):
    db_team = db.query(team_models.Team).filter(team_models.Team.id == team_id).first()

    if team.team_school is not None:
        db_team.team_school = team.team_school

    if team.team_event is not None:
        db_team.team_event = team.team_event

    db.add(db_team)
    db.commit()
    db.refresh(db_team)

    return db_team


def delete_team(db: Session, team_id: int):
    db_team = db.query(team_models.Team).filter(team_models.Team.id == team_id).first()

    team_id = db_team.id

    db.delete(db_team)
    db.commit()

    return f"Deleted team with the id {team_id}!"
