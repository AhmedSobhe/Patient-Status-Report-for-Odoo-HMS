# Patient-Status-Report-for-Odoo-HMS
🏥 Patient Status Report for Odoo HMS
This project provides a professionally styled PDF report for the Hospital Management System (HMS) module in Odoo. The report is designed to give a clear and concise overview of a patient's status including personal information, department, doctors, and medical history logs.

📋 Features
Custom QWeb PDF report for hms.patient records

Displays:

Patient's name, age, email, and birth date

Department and assigned doctors

PCR and blood type

Patient's photo (if available)

Log history table with user, date, and description

Styled report with layout similar to business medical summaries

Automatically accessible via the "Print" button on the patient form

📸 Report Preview

🧩 Technical Details
QWeb report file: patient_status_report.xml

Linked to model: hms.patient

Includes related model data like:

department_id

doctor_ids

log_history_ids

Fully integrated with Odoo's report engine (PDF generation)

🚀 How to Use
Install the module containing this report.

Go to HMS → Patients.

Open any patient record.

Click Print → Patient Status Report.


