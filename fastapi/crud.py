from sqlalchemy.orm import Session
import schemas
from migration import models


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserBase):
    db_user = models.User(username=user.username, is_admin=user.is_admin)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int,  user: schemas.UserBase,):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    for key, value in user.model_dump().items():
        # userを再セット,model_dump()->辞書型に変換,items()->key,値を繰り返し
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(db_user)
    db.commit()


def create_todo(db: Session, user_id: int, todo: schemas.TodoBase):
    db_todo = models.Todo(
        user_id=user_id, title=todo.title, content=todo.content)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def get_todos(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).filter(models.Todo.user_id == user_id)\
        .offset(skip).limit(limit).all()

# todo一括変更、うまくいかない
# def update_todo(db: Session, user_id: int, todo: schemas.TodoBase):
    db_todo = db.query(models.Todo).filter(
        models.Todo.user_id == user_id).all()
    for update in db_todo:
        for key, value in todo.model_dump().items():
            setattr(update, key, value)
        db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, user_id: int):
    db_todo = db.query(models.Todo).filter(
        models.Todo.user_id == user_id).all()
    for delete_todo in db_todo:
        db.delete(delete_todo)
    db.commit()


def get_todo(db: Session, user_id: int, todo_id: int):
    return db.query(models.Todo).filter(
        models.Todo.user_id == user_id, models.Todo.id == todo_id).first()
