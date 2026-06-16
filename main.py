from fastapi import FastAPI
from database.db_connection import create_tables
from routes.book_routes import router as book_router
from routes.member_routes import router as member_router
from routes.report_routes import router as report_router 
# create_tables()

app = FastAPI()

app.include_router(book_router)
app.include_router(member_router)
app.include_router(report_router)


