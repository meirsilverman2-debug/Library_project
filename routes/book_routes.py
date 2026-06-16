from fastapi import APIRouter
from database.book_db import BookDB

bookdb = BookDB()

router = APIRouter(prefix="/books", tags=["book"])


@router.post("/books")
def create_book(data: dict):
    return bookdb.create_book(data)


@router.get("/books")
def get_all_books():
    return bookdb.get_all_books()


@router.get("/books/{id}")
def get_book_by_id(id: int):
    return bookdb.get_book_by_id(id)


@router.put("/books/{id}")
def update_book(id: int, data: dict):
    return bookdb.update_book(id, data)


@router.put("/books/{id}/return/{member_id}")
def set_available(id: int, member_id: int):
    return bookdb.set_available(id=id, member_id=member_id, val=True)


@router.put("/books/{id}/borrow/{member_id}")
def set_available(id: int, member_id: int):
    return bookdb.set_available(id=id, member_id=member_id, val=False)







