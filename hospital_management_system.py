from datetime import datetime, timedelta
import random
import json

# ==================== ENUMS AND CONSTANTS ====================
class Department:
    CARDIOLOGY = "Cardiology"
    NEUROLOGY = "Neurology"
    ORTHOPEDICS = "Orthopedics"
    GENERAL = "General"
    PEDIATRICS = "Pediatrics"
    DERMATOLOGY = "Dermatology"

class AppointmentStatus:
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

# ==================== PATIENT CLASS ====================
class Patient:
    patient_id_counter = 1000
    
    def __init__(self, name, age, gender, contact, symptoms):
        self.patient_id = Patient.patient_id_counter
        Patient.patient_id_counter += 1
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact
        self.symptoms = symptoms
        self.registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.medical_history = []
        self.appointments = []
        self.blood_group = ""
        self.allergies = ""
    
    def add_medical_record(self, record):
        self.medical_history.append(record)
    
    def display_info(self):
        print(f"\n{'='*60}")
        print(f"PATIENT INFORMATION")
        print(f"{'='*60}")
        print(f"Patient ID          : {self.patient_id}")
        print(f"Name                : {self.name}")
        print(f"Age                 : {self.age} years")
        print(f"Gender              : {self.gender}")
        print(f"Contact             : {self.contact}")
        print(f"Symptoms            : {self.symptoms}")
        print(f"Blood Group         : {self.blood_group if self.blood_group else 'Not provided'}")
        print(f"Allergies           : {self.allergies if self.allergies else 'None'}")
        print(f"Registration Date   : {self.registration_date}")
        print(f"{'='*60}\n")
    
    def __str__(self):
        return f"ID: {self.patient_id} | Name: {self.name} | Age: {self.age} | Symptoms: {self.symptoms}"

# ==================== DOCTOR CLASS ====================
class Doctor:
    doctor_id_counter = 500
    
    def __init__(self, name, department, specialization, contact, experience):
        self.doctor_id = Doctor.doctor_id_counter
        Doctor.doctor_id_counter += 1
        self.name = name
        self.department = department
        self.specialization = specialization
        self.contact = contact
        self.experience = experience
        self.schedule = {}
        self.consultation_fee = 500
    
    def add_availability(self, date, time_slots):
        """Add available time slots for a doctor on a specific date"""
        if date not in self.schedule:
            self.schedule[date] = {"slots": time_slots, "booked": []}
    
    def get_available_slots(self, date):
        """Get available slots for a specific date"""
        if date in self.schedule:
            available = [slot for slot in self.schedule[date]["slots"] 
                        if slot not in self.schedule[date]["booked"]]
            return available
        return []
    
    def book_slot(self, date, time):
        """Book a time slot"""
        if date in self.schedule:
            if time in self.get_available_slots(date):
                self.schedule[date]["booked"].append(time)
                return True
        return False
    
    def display_info(self):
        print(f"\n{'='*60}")
        print(f"DOCTOR INFORMATION")
        print(f"{'='*60}")
        print(f"Doctor ID           : {self.doctor_id}")
        print(f"Name                : Dr. {self.name}")
        print(f"Department          : {self.department}")
        print(f"Specialization      : {self.specialization}")
        print(f"Experience          : {self.experience} years")
        print(f"Contact             : {self.contact}")
        print(f"Consultation Fee    : ₹{self.consultation_fee}")
        print(f"{'='*60}\n")
    
    def __str__(self):
        return f"ID: {self.doctor_id} | Dr. {self.name} | {self.department} | ₹{self.consultation_fee}"

# ==================== APPOINTMENT CLASS ====================
class Appointment:
    appointment_id_counter = 2000
    
    def __init__(self, patient, doctor, appointment_date, appointment_time, reason):
        self.appointment_id = Appointment.appointment_id_counter
        Appointment.appointment_id_counter += 1
        self.patient = patient
        self.doctor = doctor
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.reason = reason
        self.status = AppointmentStatus.SCHEDULED
        self.booking_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.diagnosis = ""
        self.prescription = ""
        self.consultation_notes = ""
    
    def complete_appointment(self, diagnosis, prescription, notes):
        """Mark appointment as completed"""
        self.status = AppointmentStatus.COMPLETED
        self.diagnosis = diagnosis
        self.prescription = prescription
        self.consultation_notes = notes
        
        # Add to patient's medical history
        record = {
            "appointment_id": self.appointment_id,
            "date": self.appointment_date,
            "doctor": self.doctor.name,
            "diagnosis": diagnosis,
            "prescription": prescription,
            "notes": notes
        }
        self.patient.add_medical_record(record)
    
    def cancel_appointment(self):
        """Cancel appointment"""
        self.status = AppointmentStatus.CANCELLED
    
    def display_info(self):
        print(f"\n{'='*60}")
        print(f"APPOINTMENT DETAILS")
        print(f"{'='*60}")
        print(f"Appointment ID      : {self.appointment_id}")
        print(f"Patient             : {self.patient.name} (ID: {self.patient.patient_id})")
        print(f"Doctor              : Dr. {self.doctor.name}")
        print(f"Department          : {self.doctor.department}")
        print(f"Date                : {self.appointment_date}")
        print(f"Time                : {self.appointment_time}")
        print(f"Reason              : {self.reason}")
        print(f"Status              : {self.status}")
        print(f"Booking Date        : {self.booking_date}")
        if self.status == AppointmentStatus.COMPLETED:
            print(f"Diagnosis           : {self.diagnosis}")
            print(f"Prescription        : {self.prescription}")
        print(f"{'='*60}\n")
    
    def __str__(self):
        return f"ID: {self.appointment_id} | Patient: {self.patient.name} | Doctor: Dr. {self.doctor.name} | {self.appointment_date} {self.appointment_time} | {self.status}"

# ==================== BILLING CLASS ====================
class Bill:
    bill_id_counter = 3000
    
    def __init__(self, patient, appointment):
        self.bill_id = Bill.bill_id_counter
        Bill.bill_id_counter += 1
        self.patient = patient
        self.appointment = appointment
        self.consultation_fee = appointment.doctor.consultation_fee
        self.test_charges = 0
        self.medicine_charges = 0
        self.room_charges = 0
        self.bill_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.payment_status = "Pending"
    
    def calculate_total(self):
        return self.consultation_fee + self.test_charges + self.medicine_charges + self.room_charges
    
    def make_payment(self):
        self.payment_status = "Paid"
    
    def display_bill(self):
        print(f"\n{'='*60}")
        print(f"MEDICAL BILL")
        print(f"{'='*60}")
        print(f"Bill ID             : {self.bill_id}")
        print(f"Patient Name        : {self.patient.name}")
        print(f"Patient ID          : {self.patient.patient_id}")
        print(f"Appointment ID      : {self.appointment.appointment_id}")
        print(f"Doctor              : Dr. {self.appointment.doctor.name}")
        print(f"Bill Date           : {self.bill_date}")
        print(f"\n--- CHARGES BREAKDOWN ---")
        print(f"Consultation Fee    : ₹{self.consultation_fee}")
        print(f"Test Charges        : ₹{self.test_charges}")
        print(f"Medicine Charges    : ₹{self.medicine_charges}")
        print(f"Room Charges        : ₹{self.room_charges}")
        print(f"-" * 60)
        print(f"TOTAL AMOUNT        : ₹{self.calculate_total()}")
        print(f"Payment Status      : {self.payment_status}")
        print(f"{'='*60}\n")

# ==================== HOSPITAL MANAGEMENT SYSTEM ====================
class HospitalManagementSystem:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.patients = {}
        self.doctors = {}
        self.appointments = []
        self.bills = []
        self.initialize_doctors()
    
    def initialize_doctors(self):
        """Initialize hospital with some default doctors"""
        doctors_data = [
            ("Dr. Rajesh Kumar", Department.CARDIOLOGY, "Cardiothoracic Surgeon", "9876543210", 15),
            ("Dr. Priya Sharma", Department.NEUROLOGY, "Neurologist", "9876543211", 12),
            ("Dr. Amit Patel", Department.ORTHOPEDICS, "Orthopedic Specialist", "9876543212", 10),
            ("Dr. Neha Singh", Department.GENERAL, "General Practitioner", "9876543213", 8),
            ("Dr. Vikram Desai", Department.PEDIATRICS, "Pediatrician", "9876543214", 9),
            ("Dr. Anjali Gupta", Department.DERMATOLOGY, "Dermatologist", "9876543215", 7),
        ]
        
        for name, dept, spec, contact, exp in doctors_data:
            doctor = Doctor(name.replace("Dr. ", ""), dept, spec, contact, exp)
            self.doctors[doctor.doctor_id] = doctor
            
            # Add sample availability
            for day in range(7):
                date = (datetime.now() + timedelta(days=day+1)).strftime("%Y-%m-%d")
                time_slots = ["09:00 AM", "10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"]
                doctor.add_availability(date, time_slots)
    
    # ==================== PATIENT OPERATIONS ====================
    def register_patient(self):
        """Register a new patient"""
        print(f"\n{'='*60}")
        print(f"PATIENT REGISTRATION")
        print(f"{'='*60}")
        
        name = input("Enter patient name: ").strip()
        while not name:
            name = input("Name cannot be empty. Enter patient name: ").strip()
        
        try:
            age = int(input("Enter age: "))
            if age <= 0 or age > 150:
                print("Invalid age. Please enter a valid age.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid age.")
            return
        
        print("Select gender: 1. Male  2. Female  3. Other")
        gender_choice = input("Enter choice (1/2/3): ").strip()
        gender_map = {"1": "Male", "2": "Female", "3": "Other"}
        gender = gender_map.get(gender_choice, "Not specified")
        
        contact = input("Enter contact number: ").strip()
        while not contact or len(contact) < 10:
            contact = input("Enter valid contact number (minimum 10 digits): ").strip()
        
        symptoms = input("Enter symptoms: ").strip()
        while not symptoms:
            symptoms = input("Symptoms cannot be empty. Enter symptoms: ").strip()
        
        # Create patient
        patient = Patient(name, age, gender, contact, symptoms)
        self.patients[patient.patient_id] = patient
        
        print(f"\n{'='*60}")
        print(f"✓ PATIENT REGISTERED SUCCESSFULLY")
        print(f"{'='*60}")
        print(f"Patient ID Generated: {patient.patient_id}")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Symptoms: {symptoms}")
        print(f"{'='*60}\n")
        
        return patient.patient_id
    
    def view_patient(self):
        """View patient information"""
        try:
            patient_id = int(input("Enter Patient ID: "))
            if patient_id in self.patients:
                self.patients[patient_id].display_info()
            else:
                print(f"Patient with ID {patient_id} not found.")
        except ValueError:
            print("Invalid input. Please enter a valid Patient ID.")
    
    def view_all_patients(self):
        """View all registered patients"""
        if not self.patients:
            print("\nNo patients registered yet.")
            return
        
        print(f"\n{'='*60}")
        print(f"ALL REGISTERED PATIENTS")
        print(f"{'='*60}")
        for patient_id, patient in sorted(self.patients.items()):
            print(patient)
        print(f"{'='*60}\n")
    
    def update_patient_info(self):
        """Update patient information"""
        try:
            patient_id = int(input("Enter Patient ID: "))
            if patient_id not in self.patients:
                print(f"Patient with ID {patient_id} not found.")
                return
            
            patient = self.patients[patient_id]
            print(f"\nUpdating information for {patient.name}:")
            
            print("1. Update Blood Group")
            print("2. Update Allergies")
            print("3. Update Contact Number")
            
            choice = input("Enter choice (1/2/3): ").strip()
            
            if choice == "1":
                patient.blood_group = input("Enter blood group: ").strip()
                print("✓ Blood group updated.")
            elif choice == "2":
                patient.allergies = input("Enter allergies: ").strip()
                print("✓ Allergies updated.")
            elif choice == "3":
                patient.contact = input("Enter new contact number: ").strip()
                print("✓ Contact number updated.")
            else:
                print("Invalid choice.")
        
        except ValueError:
            print("Invalid input.")
    
    # ==================== DOCTOR OPERATIONS ====================
    def view_all_doctors(self):
        """View all doctors"""
        print(f"\n{'='*60}")
        print(f"ALL DOCTORS IN {self.hospital_name.upper()}")
        print(f"{'='*60}")
        for doctor_id, doctor in sorted(self.doctors.items()):
            print(doctor)
        print(f"{'='*60}\n")
    
    def view_doctor_details(self):
        """View specific doctor details"""
        try:
            doctor_id = int(input("Enter Doctor ID: "))
            if doctor_id in self.doctors:
                self.doctors[doctor_id].display_info()
                self.view_doctor_schedule(doctor_id)
            else:
                print(f"Doctor with ID {doctor_id} not found.")
        except ValueError:
            print("Invalid input. Please enter a valid Doctor ID.")
    
    def view_doctor_schedule(self, doctor_id):
        """View doctor's schedule"""
        if doctor_id not in self.doctors:
            print("Doctor not found.")
            return
        
        doctor = self.doctors[doctor_id]
        print(f"\n--- SCHEDULE FOR DR. {doctor.name.upper()} ---")
        
        if not doctor.schedule:
            print("No schedule available.")
            return
        
        for date in sorted(doctor.schedule.keys()):
            available_slots = doctor.get_available_slots(date)
            print(f"\nDate: {date}")
            print(f"Available slots: {', '.join(available_slots)}")
    
    def search_doctors_by_department(self):
        """Search doctors by department"""
        print(f"\n{'='*60}")
        print(f"SEARCH DOCTORS BY DEPARTMENT")
        print(f"{'='*60}")
        print("1. Cardiology")
        print("2. Neurology")
        print("3. Orthopedics")
        print("4. General")
        print("5. Pediatrics")
        print("6. Dermatology")
        print(f"{'='*60}")
        
        choice = input("Enter choice (1-6): ").strip()
        dept_map = {
            "1": Department.CARDIOLOGY,
            "2": Department.NEUROLOGY,
            "3": Department.ORTHOPEDICS,
            "4": Department.GENERAL,
            "5": Department.PEDIATRICS,
            "6": Department.DERMATOLOGY
        }
        
        department = dept_map.get(choice)
        if not department:
            print("Invalid choice.")
            return
        
        print(f"\n--- DOCTORS IN {department.upper()} ---")
        found = False
        for doctor_id, doctor in self.doctors.items():
            if doctor.department == department:
                print(doctor)
                found = True
        
        if not found:
            print(f"No doctors found in {department} department.")
    
    # ==================== APPOINTMENT OPERATIONS ====================
    def book_appointment(self):
        """Book an appointment for a patient"""
        print(f"\n{'='*60}")
        print(f"BOOK APPOINTMENT")
        print(f"{'='*60}")
        
        try:
            patient_id = int(input("Enter Patient ID: "))
            if patient_id not in self.patients:
                print(f"Patient with ID {patient_id} not found.")
                return
            
            patient = self.patients[patient_id]
            
            doctor_id = int(input("Enter Doctor ID: "))
            if doctor_id not in self.doctors:
                print(f"Doctor with ID {doctor_id} not found.")
                return
            
            doctor = self.doctors[doctor_id]
            
            appointment_date = input("Enter appointment date (YYYY-MM-DD): ").strip()
            available_slots = doctor.get_available_slots(appointment_date)
            
            if not available_slots:
                print(f"No available slots on {appointment_date}.")
                return
            
            print(f"\nAvailable slots on {appointment_date}:")
            for idx, slot in enumerate(available_slots, 1):
                print(f"{idx}. {slot}")
            
            slot_choice = int(input("Select time slot: "))
            if slot_choice < 1 or slot_choice > len(available_slots):
                print("Invalid choice.")
                return
            
            appointment_time = available_slots[slot_choice - 1]
            reason = input("Enter reason for appointment: ").strip()
            
            # Book the appointment
            appointment = Appointment(patient, doctor, appointment_date, appointment_time, reason)
            self.appointments.append(appointment)
            
            # Book the slot with doctor
            doctor.book_slot(appointment_date, appointment_time)
            
            print(f"\n{'='*60}")
            print(f"✓ APPOINTMENT BOOKED SUCCESSFULLY")
            print(f"{'='*60}")
            print(f"Appointment ID      : {appointment.appointment_id}")
            print(f"Patient ID          : {patient_id}")
            print(f"Doctor              : Dr. {doctor.name}")
            print(f"Date                : {appointment_date}")
            print(f"Time                : {appointment_time}")
            print(f"{'='*60}\n")
            
            return appointment.appointment_id
        
        except ValueError:
            print("Invalid input.")
    
    def view_appointment(self):
        """View appointment details"""
        try:
            appointment_id = int(input("Enter Appointment ID: "))
            for appointment in self.appointments:
                if appointment.appointment_id == appointment_id:
                    appointment.display_info()
                    return
            print(f"Appointment with ID {appointment_id} not found.")
        except ValueError:
            print("Invalid input.")
    
    def view_patient_appointments(self):
        """View all appointments of a patient"""
        try:
            patient_id = int(input("Enter Patient ID: "))
            if patient_id not in self.patients:
                print(f"Patient with ID {patient_id} not found.")
                return
            
            patient = self.patients[patient_id]
            patient_appointments = [apt for apt in self.appointments if apt.patient.patient_id == patient_id]
            
            if not patient_appointments:
                print(f"No appointments found for patient {patient.name}.")
                return
            
            print(f"\n{'='*60}")
            print(f"APPOINTMENTS FOR {patient.name.upper()}")
            print(f"{'='*60}")
            for apt in patient_appointments:
                print(apt)
            print(f"{'='*60}\n")
        
        except ValueError:
            print("Invalid input.")
    
    def view_all_appointments(self):
        """View all appointments"""
        if not self.appointments:
            print("\nNo appointments scheduled yet.")
            return
        
        print(f"\n{'='*60}")
        print(f"ALL APPOINTMENTS")
        print(f"{'='*60}")
        for apt in self.appointments:
            print(apt)
        print(f"{'='*60}\n")
    
    def complete_appointment(self):
        """Mark appointment as completed with diagnosis and prescription"""
        try:
            appointment_id = int(input("Enter Appointment ID: "))
            
            appointment = None
            for apt in self.appointments:
                if apt.appointment_id == appointment_id:
                    appointment = apt
                    break
            
            if not appointment:
                print(f"Appointment with ID {appointment_id} not found.")
                return
            
            if appointment.status == AppointmentStatus.COMPLETED:
                print("This appointment is already completed.")
                return
            
            print(f"\nCompleting appointment for {appointment.patient.name}")
            diagnosis = input("Enter diagnosis: ").strip()
            prescription = input("Enter prescription: ").strip()
            notes = input("Enter consultation notes: ").strip()
            
            appointment.complete_appointment(diagnosis, prescription, notes)
            
            print(f"\n{'='*60}")
            print(f"✓ APPOINTMENT COMPLETED")
            print(f"{'='*60}")
            print(f"Appointment ID: {appointment_id}")
            print(f"Diagnosis: {diagnosis}")
            print(f"Prescription: {prescription}")
            print(f"{'='*60}\n")
        
        except ValueError:
            print("Invalid input.")
    
    def cancel_appointment(self):
        """Cancel an appointment"""
        try:
            appointment_id = int(input("Enter Appointment ID to cancel: "))
            
            appointment = None
            for apt in self.appointments:
                if apt.appointment_id == appointment_id:
                    appointment = apt
                    break
            
            if not appointment:
                print(f"Appointment with ID {appointment_id} not found.")
                return
            
            if appointment.status == AppointmentStatus.CANCELLED:
                print("This appointment is already cancelled.")
                return
            
            appointment.cancel_appointment()
            print(f"\n✓ Appointment {appointment_id} cancelled successfully.")
        
        except ValueError:
            print("Invalid input.")
    
    # ==================== MEDICAL HISTORY ====================
    def view_medical_history(self):
        """View patient's medical history"""
        try:
            patient_id = int(input("Enter Patient ID: "))
            if patient_id not in self.patients:
                print(f"Patient with ID {patient_id} not found.")
                return
            
            patient = self.patients[patient_id]
            
            if not patient.medical_history:
                print(f"\nNo medical history for {patient.name}.")
                return
            
            print(f"\n{'='*60}")
            print(f"MEDICAL HISTORY - {patient.name.upper()}")
            print(f"{'='*60}")
            for idx, record in enumerate(patient.medical_history, 1):
                print(f"\n--- Record {idx} ---")
                print(f"Date: {record['date']}")
                print(f"Doctor: Dr. {record['doctor']}")
                print(f"Diagnosis: {record['diagnosis']}")
                print(f"Prescription: {record['prescription']}")
                print(f"Notes: {record['notes']}")
            print(f"\n{'='*60}\n")
        
        except ValueError:
            print("Invalid input.")
    
    # ==================== BILLING OPERATIONS ====================
    def generate_bill(self):
        """Generate bill for a completed appointment"""
        try:
            appointment_id = int(input("Enter Appointment ID: "))
            
            appointment = None
            for apt in self.appointments:
                if apt.appointment_id == appointment_id:
                    appointment = apt
                    break
            
            if not appointment:
                print(f"Appointment with ID {appointment_id} not found.")
                return
            
            if appointment.status != AppointmentStatus.COMPLETED:
                print("Bill can only be generated for completed appointments.")
                return
            
            # Check if bill already exists
            for bill in self.bills:
                if bill.appointment.appointment_id == appointment_id:
                    print("Bill already generated for this appointment.")
                    return
            
            bill = Bill(appointment.patient, appointment)
            
            print(f"\nEnter additional charges (press Enter to skip):")
            
            try:
                test_charges = input("Test charges (₹): ").strip()
                if test_charges:
                    bill.test_charges = float(test_charges)
            except ValueError:
                pass
            
            try:
                medicine_charges = input("Medicine charges (₹): ").strip()
                if medicine_charges:
                    bill.medicine_charges = float(medicine_charges)
            except ValueError:
                pass
            
            try:
                room_charges = input("Room charges (₹): ").strip()
                if room_charges:
                    bill.room_charges = float(room_charges)
            except ValueError:
                pass
            
            self.bills.append(bill)
            bill.display_bill()
            
            print(f"Bill ID: {bill.bill_id}")
            return bill.bill_id
        
        except ValueError:
            print("Invalid input.")
    
    def view_bill(self):
        """View bill details"""
        try:
            bill_id = int(input("Enter Bill ID: "))
            for bill in self.bills:
                if bill.bill_id == bill_id:
                    bill.display_bill()
                    return
            print(f"Bill with ID {bill_id} not found.")
        except ValueError:
            print("Invalid input.")
    
    def process_payment(self):
        """Process payment for a bill"""
        try:
            bill_id = int(input("Enter Bill ID: "))
            for bill in self.bills:
                if bill.bill_id == bill_id:
                    if bill.payment_status == "Paid":
                        print("This bill is already paid.")
                        return
                    
                    print(f"\nAmount to be paid: ₹{bill.calculate_total()}")
                    amount = float(input("Enter amount to pay (₹): "))
                    
                    if amount < bill.calculate_total():
                        print(f"Insufficient amount. Required: ₹{bill.calculate_total()}")
                        return
                    
                    bill.make_payment()
                    change = amount - bill.calculate_total()
                    
                    print(f"\n{'='*60}")
                    print(f"✓ PAYMENT SUCCESSFUL")
                    print(f"{'='*60}")
                    print(f"Amount Paid       : ₹{amount}")
                    print(f"Total Amount      : ₹{bill.calculate_total()}")
                    print(f"Change            : ₹{change}")
                    print(f"Payment Status    : Paid")
                    print(f"{'='*60}\n")
                    return
            
            print(f"Bill with ID {bill_id} not found.")
        except ValueError:
            print("Invalid input.")
    
    # ==================== HOSPITAL STATISTICS ====================
    def view_statistics(self):
        """View hospital statistics"""
        scheduled_apts = sum(1 for apt in self.appointments if apt.status == AppointmentStatus.SCHEDULED)
        completed_apts = sum(1 for apt in self.appointments if apt.status == AppointmentStatus.COMPLETED)
        cancelled_apts = sum(1 for apt in self.appointments if apt.status == AppointmentStatus.CANCELLED)
        
        total_revenue = sum(bill.calculate_total() for bill in self.bills if bill.payment_status == "Paid")
        pending_payments = sum(bill.calculate_total() for bill in self.bills if bill.payment_status == "Pending")
        
        print(f"\n{'='*60}")
        print(f"{self.hospital_name.upper()} - STATISTICS")
        print(f"{'='*60}")
        print(f"Total Patients Registered   : {len(self.patients)}")
        print(f"Total Doctors               : {len(self.doctors)}")
        print(f"\n--- APPOINTMENTS ---")
        print(f"Scheduled Appointments      : {scheduled_apts}")
        print(f"Completed Appointments      : {completed_apts}")
        print(f"Cancelled Appointments      : {cancelled_apts}")
        print(f"Total Appointments          : {len(self.appointments)}")
        print(f"\n--- BILLING ---")
        print(f"Total Bills Generated       : {len(self.bills)}")
        print(f"Total Revenue (Paid)        : ₹{total_revenue}")
        print(f"Pending Payments            : ₹{pending_payments}")
        print(f"{'='*60}\n")


# ==================== MAIN MENU ====================
def main_menu(hospital):
    while True:
        print(f"\n{'='*60}")
        print(f"{hospital.hospital_name.upper()} - MANAGEMENT SYSTEM")
        print(f"{'='*60}")
        print("1.  Patient Management")
        print("2.  Doctor Management")
        print("3.  Appointment Management")
        print("4.  Medical History")
        print("5.  Billing & Payment")
        print("6.  Hospital Statistics")
        print("0.  Exit")
        print(f"{'='*60}")
        
        choice = input("Enter your choice (0-6): ").strip()
        
        if choice == "1":
            patient_menu(hospital)
        elif choice == "2":
            doctor_menu(hospital)
        elif choice == "3":
            appointment_menu(hospital)
        elif choice == "4":
            hospital.view_medical_history()
        elif choice == "5":
            billing_menu(hospital)
        elif choice == "6":
            hospital.view_statistics()
        elif choice == "0":
            print("\nThank you for using Hospital Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def patient_menu(hospital):
    while True:
        print(f"\n{'='*60}")
        print("PATIENT MANAGEMENT")
        print(f"{'='*60}")
        print("1. Register New Patient")
        print("2. View Patient Details")
        print("3. View All Patients")
        print("4. Update Patient Information")
        print("0. Back to Main Menu")
        print(f"{'='*60}")
        
        choice = input("Enter your choice (0-4): ").strip()
        
        if choice == "1":
            hospital.register_patient()
        elif choice == "2":
            hospital.view_patient()
        elif choice == "3":
            hospital.view_all_patients()
        elif choice == "4":
            hospital.update_patient_info()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def doctor_menu(hospital):
    while True:
        print(f"\n{'='*60}")
        print("DOCTOR MANAGEMENT")
        print(f"{'='*60}")
        print("1. View All Doctors")
        print("2. View Doctor Details")
        print("3. Search Doctors by Department")
        print("0. Back to Main Menu")
        print(f"{'='*60}")
        
        choice = input("Enter your choice (0-3): ").strip()
        
        if choice == "1":
            hospital.view_all_doctors()
        elif choice == "2":
            hospital.view_doctor_details()
        elif choice == "3":
            hospital.search_doctors_by_department()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def appointment_menu(hospital):
    while True:
        print(f"\n{'='*60}")
        print("APPOINTMENT MANAGEMENT")
        print(f"{'='*60}")
        print("1. Book New Appointment")
        print("2. View Appointment Details")
        print("3. View Patient Appointments")
        print("4. View All Appointments")
        print("5. Complete Appointment")
        print("6. Cancel Appointment")
        print("0. Back to Main Menu")
        print(f"{'='*60}")
        
        choice = input("Enter your choice (0-6): ").strip()
        
        if choice == "1":
            hospital.book_appointment()
        elif choice == "2":
            hospital.view_appointment()
        elif choice == "3":
            hospital.view_patient_appointments()
        elif choice == "4":
            hospital.view_all_appointments()
        elif choice == "5":
            hospital.complete_appointment()
        elif choice == "6":
            hospital.cancel_appointment()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def billing_menu(hospital):
    while True:
        print(f"\n{'='*60}")
        print("BILLING & PAYMENT")
        print(f"{'='*60}")
        print("1. Generate Bill")
        print("2. View Bill")
        print("3. Process Payment")
        print("0. Back to Main Menu")
        print(f"{'='*60}")
        
        choice = input("Enter your choice (0-3): ").strip()
        
        if choice == "1":
            hospital.generate_bill()
        elif choice == "2":
            hospital.view_bill()
        elif choice == "3":
            hospital.process_payment()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    hospital = HospitalManagementSystem("City Medical Center")
    main_menu(hospital)
