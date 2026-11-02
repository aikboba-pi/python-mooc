# Write your solution here
import urllib.request
import json

def retrieve_all():
    courses_response = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    json_data = courses_response.read()

    result = []

    for course in json.loads(json_data):
        if (course['enabled'] == True):
            result.append((course['fullName'], course['name'], course['year'], sum(course['exercises'])))
    
    return result

def retrieve_course(course_name: str):
    course_response = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    json_data = course_response.read()
    data = json.loads(json_data)

    result = {
        'weeks': 0,
        'students': 0,
        'hours': 0,
        'hours_average': 0,
        'exercises': 0,
        'exercises_average': 0
    }

    for week in data:
        result['weeks'] += 1

        if data[week]['students'] > result['students']:
            result['students'] = data[week]['students']
        
        result['hours'] += data[week]['hour_total']
        result['hours_average'] = result['hours'] // result['students']
        result['exercises'] += data[week]['exercise_total']
        result['exercises_average'] = result['exercises'] // result['students']

    return result