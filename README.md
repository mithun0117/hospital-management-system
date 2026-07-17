# Hospital Management System

A comprehensive Python-based Hospital Management System with features for patient registration, doctor management, appointment scheduling, medical records, and billing operations.

## Features

### 1. **Patient Management**
- Register new patients with auto-generated ID
- View patient details and information
- Update patient information (blood group, allergies, contact)
- View all registered patients
- Maintain patient medical history

### 2. **Doctor Management**
- View all doctors with departments
- Search doctors by specialty/department
- View doctor details and qualifications
- Check doctor availability and schedules
- Automatic slot management

### 3. **Appointment Management**
- Book appointments with available time slots
- View appointment details
- Complete appointments with diagnosis and prescription
- Cancel appointments
- View patient appointments
- View all appointments

### 4. **Medical Records**
- Maintain comprehensive medical history
- Store diagnosis and prescriptions
- Track consultation notes
- View complete patient medical records

### 5. **Billing System**
- Generate bills after appointment completion
- Add additional charges (tests, medicine, room)
- Process payments
- Track payment status (Pending/Paid)
- View bill details

### 6. **Hospital Statistics**
- Total patients and doctors count
- Appointment statistics (scheduled, completed, cancelled)
- Revenue tracking
- Pending payments monitoring

## System Architecture

### Classes

1. **Patient**: Manages patient information, medical history, and appointments
2. **Doctor**: Handles doctor information, schedule, and availability
3. **Appointment**: Manages appointment details and status
4. **Bill**: Handles billing and payment processing
5. **HospitalManagementSystem**: Main system controller

## Installation

### Prerequisites
- Python 3.6+
- No external dependencies required

### Setup

1. Clone the repository
```bash
git clone https://github.com/mithun0117/hospital-management-system.git
cd hospital-management-system
```

2. Run the application
```bash
python hospital_management_system.py
```

## Usage

### Main Menu
```
MAIN MENU
=========
1.  Patient Management
2.  Doctor Management
3.  Appointment Management
4.  Medical History
5.  Billing & Payment
6.  Hospital Statistics
0.  Exit
```

### Patient Registration
```
Input:
Name: John Doe
Age: 24
Gender: Male
Contact: 9876543210
Symptoms: Fever

Output:
✓ PATIENT REGISTERED SUCCESSFULLY
Patient ID Generated: 1001
```

### Book Appointment
```
Input:
Patient ID: 1001
Doctor ID: 500
Appointment Date: 2026-07-20
Time Slot: 09:00 AM
Reason: Regular Checkup

Output:
✓ APPOINTMENT BOOKED SUCCESSFULLY
Appointment ID: 2000
```

### Generate Bill
```
Input:
Appointment ID: 2000
Test Charges: 500
Medicine Charges: 300
Room Charges: 200

Output:
Bill ID: 3000
Total Amount: ₹1500
```

## Default Doctors

The system comes with pre-loaded doctors:

| Doctor ID | Name | Department | Specialization | Experience |
|-----------|------|-----------|-----------------|------------|
| 500 | Rajesh Kumar | Cardiology | Cardiothoracic Surgeon | 15 years |
| 501 | Priya Sharma | Neurology | Neurologist | 12 years |
| 502 | Amit Patel | Orthopedics | Orthopedic Specialist | 10 years |
| 503 | Neha Singh | General | General Practitioner | 8 years |
| 504 | Vikram Desai | Pediatrics | Pediatrician | 9 years |
| 505 | Anjali Gupta | Dermatology | Dermatologist | 7 years |

## Departments

- Cardiology
- Neurology
- Orthopedics
- General
- Pediatrics
- Dermatology

## Appointment Status

- **Scheduled**: Initial status after booking
- **Completed**: Status after consultation is done
- **Cancelled**: Status if appointment is cancelled

## File Structure

```
hospital-management-system/
├── hospital_management_system.py   (Main application file)
├── README.md                        (Documentation)
├── requirements.txt                 (Dependencies)
└── LICENSE                          (License file)
```

## How to Use

### 1. Register a Patient
- Select "1. Patient Management" from main menu
- Select "1. Register New Patient"
- Enter patient details

### 2. Book an Appointment
- Select "3. Appointment Management" from main menu
- Select "1. Book New Appointment"
- Enter patient ID and doctor ID
- Select available time slot

### 3. Complete Appointment
- Select "3. Appointment Management" from main menu
- Select "5. Complete Appointment"
- Enter diagnosis, prescription, and notes

### 4. Generate Bill
- Select "5. Billing & Payment" from main menu
- Select "1. Generate Bill"
- Enter appointment ID and additional charges

### 5. Process Payment
- Select "5. Billing & Payment" from main menu
- Select "3. Process Payment"
- Enter bill ID and payment amount

## ID Generation

- **Patient ID**: Auto-generated starting from 1001
- **Doctor ID**: Pre-assigned from 500-505
- **Appointment ID**: Auto-generated starting from 2000
- **Bill ID**: Auto-generated starting from 3000

## Future Enhancements

- Database integration (MySQL, PostgreSQL)
- Web interface using Flask/Django
- User authentication and authorization
- Email notifications
- SMS alerts
- Pharmacy integration
- Lab test integration
- Medical records digitalization
- Advanced reporting and analytics
- Mobile app support
- Insurance integration

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- **Mithun** - Initial work

## Support

For support, email support@hospital-management.com or create an issue on GitHub.

## Changelog

### Version 1.0.0 (2026-07-17)
- Initial release
- Core functionality implemented
- Patient, Doctor, Appointment management
- Billing system
- Medical records tracking
