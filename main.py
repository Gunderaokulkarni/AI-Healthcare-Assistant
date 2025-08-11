import streamlit as st
from qa_chain import get_medical_answer
from appointment import book_appointment, list_appointments
import pandas as pd

st.set_page_config(page_title="Healthcare Assistant", layout="centered")
st.title("AI Healthcare Assistant")

menu = st.sidebar.radio("Choose Option", ["Medical Q&A", "Book Appointment", "View Appointments"])

if menu == "Medical Q&A":
    st.header("Ask a Medical Question")
    query = st.text_input("Enter your question:")
    if st.button("Get Answer"):
        if query:
            with st.spinner("Thinking..."):
                answer = get_medical_answer(query)
            st.success(answer)
        else:
            st.warning("Please enter a question.")

elif menu == "Book Appointment":
    st.header("Book an Appointment")
    name = st.text_input("Your Name")
    doctor = st.selectbox("Select Doctor", ["Dr. Kantha (Cardiologist)", "Dr. Ganesh (Dermatologist)", "Dr. Patil (General Physician)"])
    date = st.date_input("Select Date")
    time = st.time_input("Select Time")

    if st.button("Book"):
        confirmation = book_appointment(name, doctor, str(date), str(time))
        st.success(confirmation)

elif menu == "View Appointments":
    st.header("Your Appointments")
    st.info(list_appointments())
   
