from fastapi import APIRouter
from database.member_db import MemberDB


memberdb = MemberDB()

router = APIRouter(prefix="/members", tags=["member"])


@router.post("/members")
def create_members(data: dict):
    return memberdb.create_member(data)


@router.get("/members")
def get_all_members():
    return memberdb.get_all_memmbers()


@router.get("/members/{id}")
def get_member_by_id(id: int):
    return memberdb.get_member_by_id(id)


@router.put("/members/{id}")
def update_member(id: int, data: dict):
    return memberdb.update_member(id, data)


@router.put("/members/{id}/deactivate")
def deactivate_member(id: int):
    return memberdb.deactivate_member(id)


@router.put("/members/{id}/activate")
def active_member(id: int):
    return memberdb.activate_member(id)


@router.put("/members/{id}/borrow/{member_id}")
def increment_borrows(id: int):
    memberdb.increment_borrows(id)








