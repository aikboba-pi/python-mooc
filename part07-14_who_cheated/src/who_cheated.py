# Write your solution here
import csv
from datetime import datetime, timedelta

def cheaters() -> list:
    start_times = {}
    
    # Read the start times
    with open("start_times.csv") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if not row:
                continue
            name, start_time_str = row[0], row[1]
            start_times[name] = datetime.strptime(start_time_str, "%H:%M")
    
    cheater_students = set()
    limit = timedelta(hours=3)
    
    # Read the submissions
    with open("submissions.csv") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if not row:
                continue
            name, task, points, submission_time_str = row[0], row[1], row[2], row[3]
            
            if name in start_times:
                submission_time = datetime.strptime(submission_time_str, "%H:%M")
                
                # Check if the submission was handed in more than 3 hours after start time
                if submission_time - start_times[name] > limit:
                    cheater_students.add(name)
                    
    return list(cheater_students)