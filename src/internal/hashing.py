from passlib.context import CryptContext

pwd_hashing = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def hash_pwd(pwd: str) -> str:
        return pwd_hashing.hash(pwd)

    def verify(pwd: str, hashed: str) -> str:
        return pwd_hashing.verify(pwd, hashed)