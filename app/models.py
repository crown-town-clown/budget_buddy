#holds SQLAlchemy models
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from typing import List	
from typing import Optional
from datetime import date 
from sqlalchemy import Date 


class Base(DeclarativeBase):
	pass

#create user model
class User(Base):
	__tablename__ = "users"

	id: Mapped[int] = mapped_column(primary_key=True)
	email: Mapped[str] = mapped_column(String(30))
	password_hash[str] = mapped_column(String(90))

#create transaction model
class Transaction(Base):
	__tablename__ = "transaction"

	id: Mapped[int] = mapped_column(primary_key=True)
	user_id = mapped_column(ForeignKey("users.id"))
	amount: Mapped[float] = mapped_column(Float(10))
	date: Mapped[date] = mapped_column(Date)
	description: Mapped[str] = mapped_column(String(60))

#create budget model
#create category model
class Category(Base):
	__tablename__ = "category"

	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str] = mapped_column(String(20))
	user_id = mapped_column(ForeignKey("users.id"), nullable=True)

	
#create report model