from sqlalchemy.orm import Session

from schemas.users import UserCreate
from db.models.users import User
from core.hashing import Hasher


def create_new_user(user: UserCreate, db: Session):
    user = User(
        email = user.email,
        password = Hasher.get_password_hash(user.password),
        is_active = True,
        is_superuser = False
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_with_id(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    return user

def get_all_users(db: Session):
    return db.query(User).all()
