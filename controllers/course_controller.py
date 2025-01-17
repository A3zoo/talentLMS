
from fastapi import APIRouter
from services.course_service import get_all_courses, get_courses_by_id
from services.authen_service import get_current_active_user
from typing import Annotated
from fastapi import Depends

router = APIRouter()

# Việc khai báo thêm current_user là đang thực hiện xác thực token tại 
# Depends là đang thực hiện dependency injection
# Code có vẻ nhìn hơi kỳ nhưng mà doc viết như này nên em sử dụng theo
# Có thể sửa theo dạng middleware
@router.get("/courses")
async def get_courses(current_user: Annotated[str, Depends(get_current_active_user)]):
    list_c = await get_all_courses()
    return list_c

@router.get("/courses/{id}")
async def get_a_course(id: int, current_user: Annotated[str, Depends(get_current_active_user)]):
    list_c = await get_courses_by_id(id)
    return list_c
