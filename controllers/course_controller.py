
from fastapi import APIRouter
from services.course_service import get_all_courses, get_courses_by_id, get_test_by_id, get_test_answer as get_answer
from services.authen_service import get_current_active_user
from typing import Annotated
from fastapi import Depends

router = APIRouter()

# Việc khai báo thêm current_user là đang thực hiện xác thực token tại 
# Depends là đang thực hiện dependency injection
# Code có vẻ nhìn hơi kỳ nhưng mà doc viết như này nên em sử dụng theo
# Có thể sửa theo dạng middleware

#Lấy toàn bộ khóa học
@router.get("/courses")
async def get_courses(current_user: Annotated[str, Depends(get_current_active_user)]):
    list_c = await get_all_courses()
    return list_c

#Lấy thông tin từng khóa học
@router.get("/courses/{id}")
async def get_a_course(id: int, current_user: Annotated[str, Depends(get_current_active_user)]):
    course = await get_courses_by_id(id)
    return course

#Lấy bài test
@router.get("/courses/{course_id}/test/{id}")
async def get_test(course_id: int, id: int, current_user: Annotated[str, Depends(get_current_active_user)]):
    test = await get_test_by_id(course_id, id)
    return test

#Lấy kết quả test
@router.get("/courses/{course_id}/testanswer/{id}")
async def get_test_answer(course_id: int, id: int, current_user: Annotated[str, Depends(get_current_active_user)]):
    test = await get_answer(course_id, id)
    return test
