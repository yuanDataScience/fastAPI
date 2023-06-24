from fastapi import APIRouter, Depends, status
from .. import schemas, oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import user

router = APIRouter(prefix="/user", tags=['Users'])

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session=Depends(get_db), current_user: schemas.User=
        Depends(oauth2.get_current_user)):
    return user.create(request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show_user(id: int, db: Session=Depends(get_db), current_user: schemas.User=
        Depends(oauth2.get_current_user)):
    return user.show(id, db)

