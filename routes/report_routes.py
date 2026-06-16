from fastapi import APIRouter
from database.book_db import BookDB
from database.member_db import MemberDB

memberdb = MemberDB()
bookdb = BookDB()

router = APIRouter(prefix="/reports", tags=["report"])


@router.get("/reports/summary")
def get_summary():

    summary = {}

    summary["count_total_books"] = bookdb.count_total_books()
    summary["count_avaliable_books"] = bookdb.count_available_books()
    summary["ount_borrowed_books"] = bookdb.count_borrowed_books()
    summary["count_active_members"] = memberdb.count_active_members()

    return summary






@router.get("/reports/books-by-genre")
def count_by_genre():
    return bookdb.count_by_genre()


@router.get("/reports/top-member")
def get_top_member():
    return memberdb.get_top_member()


# iven do it sayd in the paper that the method is put ok. ok
@router.get("/reports/{id}/borrow/{member_id}")
def count_active_borrows_by_member(member_id: int):
    return bookdb.count_active_borrow_by_member(member_id)


