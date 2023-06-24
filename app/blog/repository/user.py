from sqlalchemy.orm import Session
from blog import schemas, models, hashing
from fastapi import status, HTTPException


def create(request: schemas.User, db: Session):
    new_user = models.User(name=request.name, password=hashing.Hash.bcrypt(request.password),
                           email=request.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} doesnot exist")
    return user