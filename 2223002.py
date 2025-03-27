import pandas as pd

def track_absences(attendance_data):
    absence_records = []
    
    for student_id, records in attendance_data.groupby('student_id')
