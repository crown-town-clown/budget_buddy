from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import datetime

app = FastAPI()


#create classes
class User(BaseModel):
	id: int
	email: str
	password_hash: str


class Transaction(BaseModel):
	id: int
	user_id: User.id 
	amount: float
	date: datetime
	category_id: Category.id 
	description: str

class Category(BaseModel):
	id: int
	name: str
	user_id: User.id 



