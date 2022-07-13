import qrcode
import base64
from io import BytesIO

from fastapi import Depends, APIRouter, Request, status
from db.models.AdminUser import AdminUser
from db.repository.login import get_current_user_from_token
from routers.attendance import get_attendances_today_by_member_id
from routers.link import create


router = APIRouter(
    prefix='/QRCODE',
    tags=['QR Code']
    )

@router.get('/create', status_code=status.HTTP_200_OK)
def create_QR_CODE(request: Request, auth: AdminUser = Depends(get_current_user_from_token)):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
    )
    if get_attendances_today_by_member_id(auth.id) is None:
        path = create(auth=auth).link
        link = f"{request.base_url}qr/{path}"
    else:
        link = f"{request.base_url}user{auth.id}"
    
    qr.add_data(link)
    qr.make(fit = True)
    img = qr.make_image(fill_color="green", back_color = 'transparent')
    buffered = BytesIO()
    img.save(buffered, format="png")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return f"data:image/png;base64,{img_str}"
