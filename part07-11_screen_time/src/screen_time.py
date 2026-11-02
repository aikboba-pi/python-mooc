# Write your solution here
from datetime import datetime, timedelta

filename = input("Filename: ")
start_str = input("Starting date: ")
days_count = int(input("How many days: "))

start_date = datetime.strptime(start_str, "%d.%m.%Y")

print("Please type in screen time in minutes on each day (TV computer mobile):")

daily_entries = []
total_minutes = 0

for i in range(days_count):
    current_date = start_date + timedelta(days=i)
    date_formatted = current_date.strftime("%d.%m.%Y")
    
    entry = input(f"Screen time {date_formatted}: ")
    parts = entry.split()
    
    # Sum the minutes for the current day
    day_total = sum(int(x) for x in parts)
    total_minutes += day_total
    
    # Store formatted record: dd.mm.yyyy: TV/computer/mobile
    daily_entries.append(f"{date_formatted}: {'/'.join(parts)}")

# End date for the time period header
end_date = start_date + timedelta(days=days_count - 1)
average_minutes = total_minutes / days_count

# Write the collected information to the specified file
with open(filename, "w") as file:
    file.write(f"Time period: {start_date.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}\n")
    file.write(f"Total minutes: {total_minutes}\n")
    file.write(f"Average minutes: {average_minutes:.1f}\n")
    for record in daily_entries:
        file.write(f"{record}\n")

print(f"Data stored in file {filename}")