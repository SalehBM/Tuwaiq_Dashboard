from os import link
import random
import string

from fastapi import Depends, APIRouter, status

from internal import oauth2
from db.models.AdminUser import AdminUser
from db.repository import link as linkDB
from db.repository.login import get_current_user_from_token
from schemas.Link import Link

router = APIRouter(
    prefix='/link',
    tags=['QR Links']
    )

@router.post('/create', status_code=status.HTTP_200_OK)
def create(auth: AdminUser = Depends(get_current_user_from_token)):
    link = linkDB.get_by_member(auth.id)
    if link is None:
        link = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        return linkDB.create(Link(id=None, member_id=auth.id, link=link))
    else:
        return link

@router.get('/get', status_code=status.HTTP_200_OK)
def get_by_id(id: int, auth: AdminUser = Depends(oauth2.get_current_user)):
    return linkDB.get(id)

@router.get('/get_by_link', status_code=status.HTTP_200_OK)
def get_by_link(link: str, auth: AdminUser = Depends(oauth2.get_current_user)):
    return linkDB.get_by_link(link)

@router.get('/get_by_member', status_code=status.HTTP_200_OK)
def get_by_member_id(id: int, auth: AdminUser = Depends(oauth2.get_current_user)):
    return linkDB.get_by_member(id)

@router.delete('/delete', status_code=status.HTTP_200_OK)
def delete(id : int, auth: AdminUser = Depends(oauth2.get_current_user)):
    return linkDB.delete(id)