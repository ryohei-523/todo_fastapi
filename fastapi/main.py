from fastapi import Depends, FastAPI
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


@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db=db, user_id=user_id)


@app.patch("/users/{user_id}")
def update_user(user_id: int, user: schemas.UserUpdate,
                db: Session = Depends(get_db)):
    updated_user = crud.update_user(db=db, user_id=user_id, user=user)
    # existing_user = crud.get_user_by_uid(db, user_id)
    # if existing_user is None:
    # raise HTTPException(status_code=404, detail="User not found")

    return updated_user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user(db=db, user_id=user_id)
    return


@app.post("/users/{user_id}/todos")
def create_todo(user_id: int, todo: schemas.TodoBase,
                db: Session = Depends(get_db)):
    return crud.create_todo(db=db, user_id=user_id, todo=todo)


@app.get("/users/{user_id}/todos")
def get_todos(user_id: int, db: Session = Depends(get_db)):
    return crud.get_todos(db=db, user_id=user_id)


@app.patch("/users/{user_id}/todos")
def update_todo(user_id: int, todo: schemas.TodoBase,
                db: Session = Depends(get_db)):
    return crud.update_todo(db=db, user_id=user_id, todo=todo)


@app.delete("/users/{user_id}/todos")
def delete_todo(user_id: int, db: Session = Depends(get_db)):
    crud.delete_todo(db=db, user_id=user_id)
    return


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
