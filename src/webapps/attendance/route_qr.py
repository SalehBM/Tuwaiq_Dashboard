# ######################### #
#     Tuwaiq Dashboard      #
#          Qr Code          #
# ######################### #

from fastapi import APIRouter, Request

from routers.link import get_by_link, delete
from routers.admin import get_admin
from routers.attendance import create
from webapps.base import templates

router = APIRouter(include_in_schema=False)

@router.get("/qr/{link}")
async def attend(request:Request, link: str):
    link_obj = get_by_link(link)
    if link_obj is None:
        return templates.TemplateResponse("pages/error.html", {
        "request": request
        })
    else:
        username = get_admin(link_obj.member_id).username
        create(link_obj.member_id)
        delete(link_obj.id)
        return templates.TemplateResponse("pages/success.html", {
            "request": request,
            "username": username
        })