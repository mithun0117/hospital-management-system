# Hospital Management System - Usage Guide

## Getting Started

### Installation

1. **Clone the Repository**
```bash
git clone https://github.com/mithun0117/hospital-management-system.git
cd hospital-management-system
```

2. **Run the Application**
```bash
python hospital_management_system.py
```

## Main Menu Navigation

When you start the application, you'll see the main menu:

```
============================================================
CITY MEDICAL CENTER - MANAGEMENT SYSTEM
============================================================
1.  Patient Management
2.  Doctor Management
3.  Appointment Management
4.  Medical History
5.  Billing & Payment
6.  Hospital Statistics
0.  Exit
============================================================
```

---

## 1. Patient Management

### 1.1 Register New Patient

**Steps:**
1. Select option `1` from main menu
2. Select option `1` from patient menu
3. Enter the following information:
   - **Patient Name**: Full name of the patient
   - **Age**: Age in years (1-150)
   - **Gender**: Select from Male/Female/Other
   - **Contact Number**: Phone number (minimum 10 digits)
   - **Symptoms**: Primary symptoms

**Example:**
```
Enter patient name: John Doe
Enter age: 24
Select gender: 1. Male  2. Female  3. Other
Enter choice (1/2/3): 1
Enter contact number: 9876543210
Enter symptoms: Fever, Cough

Output:
✓ PATIENT REGISTERED SUCCESSFULLY
Patient ID Generated: 1001
Name: John Doe
Age: 24
Symptoms: Fever, Cough
```

**Note:** Patient ID is auto-generated and starts from 1001.

### 1.2 View Patient Details

**Steps:**
1. Select option `1` from main menu
2. Select option `2` from patient menu
3. Enter the Patient ID

**Output:**
```
============================================================
PATIENT INFORMATION
============================================================
Patient ID          : 1001
Name                : John Doe
Age                 : 24 years
Gender              : Male
Contact             : 9876543210
Symptoms            : Fever, Cough
Blood Group         : Not provided
Allergies           : None
Registration Date   : 2026-07-17 10:30:45
============================================================
```

### 1.3 View All Patients

**Steps:**
1. Select option `1` from main menu
2. Select option `3` from patient menu

**Output:**
```
============================================================
ALL REGISTERED PATIENTS
============================================================
ID: 1001 | Name: John Doe | Age: 24 | Symptoms: Fever, Cough
ID: 1002 | Name: Sarah Smith | Age: 32 | Symptoms: Headache
ID: 1003 | Name: Mike Johnson | Age: 58 | Symptoms: Chest Pain
============================================================
```

### 1.4 Update Patient Information

**Steps:**
1. Select option `1` from main menu
2. Select option `4` from patient menu
3. Enter Patient ID
4. Select what to update:
   - Option `1`: Update Blood Group
   - Option `2`: Update Allergies
   - Option `3`: Update Contact Number

**Example:**
```
Enter Patient ID: 1001
Updating information for John Doe:
1. Update Blood Group
2. Update Allergies
3. Update Contact Number
Enter choice (1/2/3): 1
Enter blood group: O+
✓ Blood group updated.
```

---

## 2. Doctor Management

### 2.1 View All Doctors

**Steps:**
1. Select option `2` from main menu
2. Select option `1` from doctor menu

**Output:**
```
============================================================
ALL DOCTORS IN CITY MEDICAL CENTER
============================================================
ID: 500 | Dr. Rajesh Kumar | Cardiology | ₹500
ID: 501 | Dr. Priya Sharma | Neurology | ₹500
ID: 502 | Dr. Amit Patel | Orthopedics | ₹500
ID: 503 | Dr. Neha Singh | General | ₹500
ID: 504 | Dr. Vikram Desai | Pediatrics | ₹500
ID: 505 | Dr. Anjali Gupta | Dermatology | ₹500
============================================================
```

### 2.2 View Doctor Details

**Steps:**
1. Select option `2` from main menu
2. Select option `2` from doctor menu
3. Enter Doctor ID

**Output:**
```
============================================================
DOCTOR INFORMATION
============================================================
Doctor ID           : 500
Name                : Dr. Rajesh Kumar
Department          : Cardiology
Specialization      : Cardiothoracic Surgeon
Experience          : 15 years
Contact             : 9876543210
Consultation Fee    : ₹500
============================================================

--- SCHEDULE FOR DR. RAJESH KUMAR ---

Date: 2026-07-18
Available slots: 09:00 AM, 10:00 AM, 11:00 AM, 02:00 PM, 03:00 PM, 04:00 PM
```

### 2.3 Search Doctors by Department

**Steps:**
1. Select option `2` from main menu
2. Select option `3` from doctor menu
3. Select desired department (1-6)

**Example:**
```
SEARCH DOCTORS BY DEPARTMENT
============================================================
1. Cardiology
2. Neurology
3. Orthopedics
4. General
5. Pediatrics
6. Dermatology
============================================================
Enter choice (1-6): 1

--- DOCTORS IN CARDIOLOGY ---
ID: 500 | Dr. Rajesh Kumar | Cardiology | ₹500
```

---

## 3. Appointment Management

### 3.1 Book New Appointment

**Steps:**
1. Select option `3` from main menu
2. Select option `1` from appointment menu
3. Enter Patient ID
4. Enter Doctor ID
5. Enter appointment date (YYYY-MM-DD format)
6. Select available time slot
7. Enter reason for appointment

**Example:**
```
============================================================
BOOK APPOINTMENT
============================================================
Enter Patient ID: 1001
Enter Doctor ID: 500
Enter appointment date (YYYY-MM-DD): 2026-07-20

Available slots on 2026-07-20:
1. 09:00 AM
2. 10:00 AM
3. 11:00 AM
4. 02:00 PM
5. 03:00 PM
6. 04:00 PM

Select time slot: 1
Enter reason for appointment: Cardiac Checkup

============================================================
✓ APPOINTMENT BOOKED SUCCESSFULLY
============================================================
Appointment ID      : 2000
Patient ID          : 1001
Doctor              : Dr. Rajesh Kumar
Date                : 2026-07-20
Time                : 09:00 AM
============================================================
```

### 3.2 View Appointment Details

**Steps:**
1. Select option `3` from main menu
2. Select option `2` from appointment menu
3. Enter Appointment ID

**Output:**
```
============================================================
APPOINTMENT DETAILS
============================================================
Appointment ID      : 2000
Patient             : John Doe (ID: 1001)
Doctor              : Dr. Rajesh Kumar
Department          : Cardiology
Date                : 2026-07-20
Time                : 09:00 AM
Reason              : Cardiac Checkup
Status              : Scheduled
Booking Date        : 2026-07-17 10:45:30
============================================================
```

### 3.3 Complete Appointment

**Steps:**
1. Select option `3` from main menu
2. Select option `5` from appointment menu
3. Enter Appointment ID
4. Enter diagnosis, prescription, and consultation notes

**Example:**
```
Enter Appointment ID: 2000
Completing appointment for John Doe
Enter diagnosis: Hypertension Stage 2
Enter prescription: Lisinopril 10mg daily, Aspirin 100mg daily
Enter consultation notes: Patient advised to reduce salt intake and exercise regularly

============================================================
✓ APPOINTMENT COMPLETED
============================================================
Appointment ID: 2000
Diagnosis: Hypertension Stage 2
Prescription: Lisinopril 10mg daily, Aspirin 100mg daily
============================================================
```

### 3.4 Cancel Appointment

**Steps:**
1. Select option `3` from main menu
2. Select option `6` from appointment menu
3. Enter Appointment ID to cancel

**Output:**
```
✓ Appointment 2000 cancelled successfully.
```

### 3.5 View Patient Appointments

**Steps:**
1. Select option `3` from main menu
2. Select option `3` from appointment menu
3. Enter Patient ID

**Output:**
```
============================================================
APPOINTMENTS FOR JOHN DOE
============================================================
ID: 2000 | Patient: John Doe | Doctor: Dr. Rajesh Kumar | 2026-07-20 09:00 AM | Completed
ID: 2001 | Patient: John Doe | Doctor: Dr. Priya Sharma | 2026-07-21 10:00 AM | Scheduled
============================================================
```

---

## 4. Medical History

**Steps:**
1. Select option `4` from main menu
2. Enter Patient ID

**Output:**
```
============================================================
MEDICAL HISTORY - JOHN DOE
============================================================

--- Record 1 ---
Date: 2026-07-20
Doctor: Dr. Rajesh Kumar
Diagnosis: Hypertension Stage 2
Prescription: Lisinopril 10mg daily, Aspirin 100mg daily
Notes: Patient advised to reduce salt intake and exercise regularly

--- Record 2 ---
Date: 2026-07-21
Doctor: Dr. Priya Sharma
Diagnosis: Tension Headache
Prescription: Paracetamol 500mg as needed
Notes: Regular follow-up recommended

============================================================
```

---

## 5. Billing & Payment

### 5.1 Generate Bill

**Steps:**
1. Select option `5` from main menu
2. Select option `1` from billing menu
3. Enter Appointment ID (must be completed)
4. Enter additional charges (optional):
   - Test charges
   - Medicine charges
   - Room charges

**Example:**
```
Enter Appointment ID: 2000

============================================================
MEDICAL BILL
============================================================
Bill ID             : 3000
Patient Name        : John Doe
Patient ID          : 1001
Appointment ID      : 2000
Doctor              : Dr. Rajesh Kumar
Bill Date           : 2026-07-17 11:00:00

--- CHARGES BREAKDOWN ---
Consultation Fee    : ₹500
Test Charges        : ₹1000
Medicine Charges    : ₹500
Room Charges        : ₹300
------------------------------------------------------------
TOTAL AMOUNT        : ₹2300
Payment Status      : Pending
============================================================

Bill ID: 3000
```

### 5.2 View Bill

**Steps:**
1. Select option `5` from main menu
2. Select option `2` from billing menu
3. Enter Bill ID

### 5.3 Process Payment

**Steps:**
1. Select option `5` from main menu
2. Select option `3` from billing menu
3. Enter Bill ID
4. Enter payment amount

**Example:**
```
Enter Bill ID: 3000

Amount to be paid: ₹2300
Enter amount to pay (₹): 2300

============================================================
✓ PAYMENT SUCCESSFUL
============================================================
Amount Paid       : ₹2300
Total Amount      : ₹2300
Change            : ₹0
Payment Status    : Paid
============================================================
```

---

## 6. Hospital Statistics

**Steps:**
1. Select option `6` from main menu

**Output:**
```
============================================================
CITY MEDICAL CENTER - STATISTICS
============================================================
Total Patients Registered   : 10
Total Doctors               : 6

--- APPOINTMENTS ---
Scheduled Appointments      : 5
Completed Appointments      : 3
Cancelled Appointments      : 1
Total Appointments          : 9

--- BILLING ---
Total Bills Generated       : 3
Total Revenue (Paid)        : ₹7500
Pending Payments            : ₹2300
============================================================
```

---

## Tips & Tricks

### Important Notes

1. **Patient ID**: Once generated, it cannot be changed. Keep it safe for future reference.
2. **Appointment Booking**: You can only book appointments on dates with available slots.
3. **Bill Generation**: Bills can only be generated after an appointment is marked as completed.
4. **Medical History**: All completed appointments are automatically added to patient's medical history.
5. **Doctor Slots**: Each doctor has 6 available slots per day (09:00 AM, 10:00 AM, 11:00 AM, 02:00 PM, 03:00 PM, 04:00 PM).

### Data Validation

- **Age**: Must be between 1 and 150
- **Contact**: Minimum 10 digits
- **Date Format**: YYYY-MM-DD (e.g., 2026-07-20)
- **Amount**: Must be greater than or equal to total bill amount

### Troubleshooting

| Issue | Solution |
|-------|----------|
| "Patient not found" | Verify the correct Patient ID |
| "No available slots" | Choose a different date or doctor |
| "Bill can only be generated for completed appointments" | Complete the appointment first |
| "Insufficient amount" | Enter amount >= total bill amount |

---

## Sample Workflow

### Complete Patient Journey

1. **Register Patient**
   - Register a new patient (ID: 1001)

2. **Search for Doctor**
   - Search doctors by department (Cardiology)
   - View available doctors and their schedules

3. **Book Appointment**
   - Book appointment with Dr. Rajesh Kumar (ID: 500)
   - Select available time slot

4. **Complete Appointment**
   - After consultation, complete the appointment with diagnosis and prescription

5. **Generate Bill**
   - Generate bill for the completed appointment
   - Add additional charges if any

6. **Process Payment**
   - Process payment using bill ID

7. **View Medical History**
   - View patient's medical history to track all past consultations

---

## Keyboard Shortcuts

- Press `0` to go back to previous menu
- Press `0` from main menu to exit the application

---

For more information, refer to the README.md file.
