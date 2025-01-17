
from fastapi import APIRouter
from services.course_service import get_all_courses, get_courses_by_id

router = APIRouter()

@router.get("/courses")
async def get_courses():
    list_c = await get_courses_by_id(125)
    return list_c

@router.get("/courses/{id}")
async def get_a_course(id: int):
    list_c = await get_courses_by_id(id)
    return list_c
