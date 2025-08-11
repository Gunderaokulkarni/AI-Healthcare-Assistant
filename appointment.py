import datetime

appointments = []

def book_appointment(patient_name, doctor, date, time):
    appointment = {
        "patient": patient_name,
        "doctor": doctor,
        "date": date,
        "time": time
    }
    appointments.append(appointment)
    return f"✅ Appointment booked for {patient_name} with {doctor} on {date} at {time}."

def list_appointments():
    if not appointments:
        return "No appointments booked yet."
    return "\n".join([f"{a['patient']} → {a['doctor']} on {a['date']} at {a['time']}" for a in appointments])
