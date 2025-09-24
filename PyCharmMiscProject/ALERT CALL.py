import datetime
import time

# Sample timetable: timeslot -> (subject, teacher email, room, start time)
timetable = [
    {"subject": "Math", "teacher": "pskathirvel58@gmail.com", "room": "101", "start_time": "09:00"},
    {"subject": "Science", "teacher": "johnson@school.edu", "room": "102", "start_time": "10:00"}
]

def send_alert(teacher_email, subject, room, start_time):
    # Replace with actual email/SMS sending code
    print(f"Alert: {teacher_email} - Your {subject} class in room {room} starts at {start_time} (in 5 minutes)")

def alert_teachers_before_class(timetable):
    while True:
        now = datetime.datetime.now()
        for entry in timetable:
            class_time = datetime.datetime.combine(now.date(), datetime.datetime.strptime(entry["start_time"], "%H:%M").time())
            alert_time = class_time - datetime.timedelta(minutes=5)
            # If it's time to alert (within 1 minute window)
            if alert_time <= now < alert_time + datetime.timedelta(minutes=1):
                send_alert(entry["teacher"], entry["subject"], entry["room"], entry["start_time"])
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    print("AI Timetable Alert System Started.")
    alert_teachers_before_class(timetable)