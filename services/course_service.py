
from utils.http_client import HttpClient

client = HttpClient()

def get_all_courses():
    course_list = client.get('courses')
    return course_list

def get_courses_by_id(id):
    course = client.get(f'courses/id:{id}')
    return course