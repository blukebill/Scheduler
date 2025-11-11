#backend/app/routes - users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email aready registered")
    return crud.create_user(db, user)

@router.get("/", response_model=list[schemas.UserResponse])
def read_users(db: Session = Depends(database.get_db)):
    return crud.get_users(db)
