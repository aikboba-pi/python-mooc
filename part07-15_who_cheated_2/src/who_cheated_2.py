# Write your solution here
import csv
from datetime import datetime, timedelta

def final_points() -> dict:
    start_times = {}
    
    # 1. Read start times for each student
    with open("start_times.csv") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if not row:
                continue
            name, start_time_str = row[0], row[1]
            start_times[name] = datetime.strptime(start_time_str, "%H:%M")
    
    # Nested dictionary to store the best score for each task:
    # { student_name: { task_number: max_points } }
    student_tasks = {name: {} for name in start_times}
    limit = timedelta(hours=3)
    
    # 2. Read submissions and filter out late ones
    with open("submissions.csv") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if not row:
                continue
            name, task, points, submission_time_str = row[0], int(row[1]), int(row[2]), row[3]
            
            if name in start_times:
                submission_time = datetime.strptime(submission_time_str, "%H:%M")
                
                # Check if submission is within the 3-hour limit
                if submission_time - start_times[name] <= limit:
                    # Update the task score if it's the first time or higher than before
                    current_best = student_tasks[name].get(task, 0)
                    if points > current_best:
                        student_tasks[name][task] = points
                        
    # 3. Sum points for each student across all tasks
    totals = {}
    for name, tasks in student_tasks.items():
        totals[name] = sum(tasks.values())
        
    return totals