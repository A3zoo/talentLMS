
from utils.http_client import HttpClient
from models.course import Course
from models.test_answer import TestAnswer

client = HttpClient()

async def get_all_courses():
    course_list = await client.get('courses')
    if not course_list:  # This checks if course_list is None or empty
        return []
    return [Course.validate(course) for course in course_list] # type: ignore


async def get_courses_by_id(id):
    course = await client.get(f'courses/id:{id}')
    return Course.validate(course) if course else None


async def get_test_by_id(course_id, id):
    course_data = await client.get(f'courses/id:{course_id}')

    if not course_data:
        return None  # No available course
    # Validate the course data with the Course model
    course = Course.validate(course_data)
    
    # Check if the course has units
    if not course.units:
        return None  # No units available in the course
    
    # Filter for the test with the specific ID in the units
    for unit in course.units:
        if unit.id == id and unit.type == 'Test': 
            return unit  # Return the matching test
    
    # If no test matches the given ID
    return None


async def get_test_answer(course_id, id):
    answer_data = await client.get(f'gettestanswers/test_id:{id},user_id:1') # Tại vì hiện tại đang sử dụng chugn 1 tk
    return TestAnswer.validate(answer_data) if answer_data else None