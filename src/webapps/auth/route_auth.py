# ######################### #
#     Tuwaiq Dashboard      #
#       Authentication      #
# ######################### #

from fastapi import APIRouter, Request, status, Response
from fastapi.responses import RedirectResponse

from routers.login import login_user_form
from webapps.base import templates

router = APIRouter(include_in_schema=False)

@router.get("/login")
async def login(request:Request):
    return templates.TemplateResponse("auth/login.html", {
        "request": request,
        })

@router.post("/login", response_class = RedirectResponse)
async def login(response: Response, request:Request):
    form = await request.form()
    username = form.get("username")
    password = form.get("password")
    try:
        data = await login_user_form(response = response, username= username, password=password),
        response = RedirectResponse(url="/dashboard", status_code=status.HTTP_302_FOUND)
        response.set_cookie(key="access_token", value=f"{data[0].get('token_type')} {data[0].get('access_token')}")
        return response
    except:
        return RedirectResponse('/login', 
        status_code=status.HTTP_302_FOUND)

@router.get("/logout", response_class = RedirectResponse)
async def logout(response: Response):
    response = RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)
    response.delete_cookie("access_token")
    return response