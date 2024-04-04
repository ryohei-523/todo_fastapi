from sqlalchemy.orm import Session
import schemas
from migration import models

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserBase):
    db_user = models.User(username = user.username,is_admin= user.is_admin)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
