#holds SQLAlchemy models
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from typing import List	
from typing import Optional


class Base(DeclarativeBase):
	pass

#create user model
class User(Base):
	__tablename__ = "users"

	id: Mapped[int] = mapped_column(primary_key=True)
	email: Mapped[str] = mapped_column(String(30))
	password_hash[str] = mapped_column(String(90))

	def __repr__(self) -> str:
		return f"User(id={self.id!r}, email={self.email!r}, password_hash={self.password_hash!r})"

#create transaction model
#create budget model
#create category model
#create report model