from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud
from migration import models
import schemas
from database import SessionLocal, engine
import uvicorn

models.BaseModel.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/users")
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)


@app.patch("/{users}")
def update_user(user_id: int, user: schemas.UserUpdate,
                db: Session = Depends(get_db)):
    updated_user = crud.update_user(db, user_id, user)
    existing_user = crud.get_user_by_uid(db, user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return updated_user


# @app.patch("/users")
# def patch_user(user: schemas.UserBase,
#               original: models.User,
#               db: Session = Depends(get_db)):
#    return crud.update_user(db=db, user=user, original=original)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
