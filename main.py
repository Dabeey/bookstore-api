from fastapi import FastAPI
from database import create_table
from routes import router


app = FastAPI()

create_table()

app.include_router(router)