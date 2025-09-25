from fastapi import FastAPI
from database import create_table
from routers import book, user


app = FastAPI()

create_table()

app.include_router(book.router)
app.include_router(user.router)