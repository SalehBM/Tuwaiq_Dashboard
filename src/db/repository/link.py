from sqlalchemy.orm import Session

from db.admin_database import get_db
from schemas.Link import Link
from db.models.Link import Link

DB = next(get_db())

def create(request: Link, db: Session = DB):
    link_db = Link(
        member_id = request.member_id,
        link = request.link,
    )
    db.add(link_db)
    db.commit()
    db.refresh(link_db)
    return link_db

def get(id: int, db: Session = DB):
    return db.query(Link).filter(Link.id==id).first()

def get_by_link(link: str, db: Session = DB):
    return db.query(Link).filter(Link.link==link).first()

def get_by_member(member_id: str, db: Session = DB):
    return db.query(Link).filter(Link.member_id==member_id).first()

def delete(id : int, db : Session = DB):
    delete_link = db.query(Link).filter(Link.id == id)
    if not delete_link.first():
        return 0
    delete_link.delete(synchronize_session=False)
    db.commit()
    return delete_link