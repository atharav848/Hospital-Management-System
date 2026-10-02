Hospital Management System

Hospital Management System is a production-ready, fully functional full-stack web application designed for hospitals to manage clinical operations, patient registrations, appointments scheduling, doctor prescriptions, billing invoices, and analytical reports.

The application features a modern, responsive user interface with complete Role-Based Access Control (RBAC) and support for a Light/Dark theme.

---

## Technical Stack
- **Frontend**: HTML5, CSS3, Bootstrap 5, Javascript, Chart.js (Dashboards)
- **Backend**: Python Flask
- **ORM & Database**: SQLAlchemy, MySQL (with Pure Python PyMySQL driver)
- **Authentication**: Flask-Login, Werkzeug (Password Hashing), Session-based Auth
- **Reporting**: ReportLab (PDF generation), Pandas & OpenPyXL (Excel/CSV compiled exports)
- **Forms & Validation**: Flask-WTF, WTForms, Email-Validator

---

## Directory Structure
```
Hospital Management System/
├── run.py                       # App Entry Point (Starts server & Auto-seeds data)
├── config.py                    # Flask Configuration (MySQL URI, SQLite fallbacks)
├── requirements.txt             # Python Package Dependencies
├── schema.sql                   # Raw MySQL DDL database schema
├── init_db.py                   # Seeder Script (Initializes tables & mocks data)
└── app/                         # Main Application Package
    ├── __init__.py              # App Factory and Extensions setup
    ├── models/                  # SQLAlchemy ORM Models
    ├── forms/                   # WTForms validation schemes
    ├── routes/                  # Controller Blueprints (RBAC endpoints)
    ├── services/                # Business logic services (Billing, PDF, Excel)
    ├── static/                  # Static Assets (Style, JS, uploads)
    └── templates/               # Jinja2 HTML layouts
```

---

## Quick Setup Instructions

### 1. Prerequisites
Ensure **Python 3.10+** is installed on your computer.

### 2. Installation
Open a command prompt/terminal in the project root directory and run:

```bash
# Install dependencies
pip install -r requirements.txt
```

### 3. Run the Application
Start the Flask server by executing:

```bash
python run.py
```

> [!NOTE]
> On startup, `run.py` will automatically test the database connection.
> - If a local MySQL server is configured and running, it will create tables inside MySQL.
> - **SQLite Fallback**: If MySQL is unreachable, it will automatically fall back and create a local SQLite database (`medicare.db`). This makes the app **immediately runnable out-of-the-box** without any database configuration overhead!

Open your browser and navigate to: `http://localhost:5000`

---

## User Roles & Login Credentials

The seeder initializes the system with a clean Admin account. No mock doctor, receptionist, or patient accounts are pre-seeded, allowing you to test clinical records using real data:

| Role | Email Address | Password | Features |
| :--- | :--- | :--- | :--- |
| **Admin** | ----------- | `---------` | Doctor/Staff/Room CRUD, System Settings, Analytics, Audit Logs |
| **Doctor / Receptionist** | *Registered by Admin* | *Set during registration* | Respective workflow dashboards |
| **Patient** | *Registered by Front Desk or Sign Up* | *Set during signup* | Patient scheduling & history dashboard |

---

## Database Configuration (MySQL)

By default, the application connects to a local MySQL server using:
- **Host**: `localhost:----`
- **Database Name**: `healthcare management system_db`
- **User**: `root`
- **Password**: `""` (Empty password)

To customize the MySQL connection credentials, you can configure these environment variables before starting the server:
- `DB_USER`: Your MySQL username (default: `root`)
- `DB_PASSWORD`: Your MySQL password (default: `""`)
- `DB_HOST`: Your MySQL host address (default: `localhost`)
- `DB_PORT`: Your MySQL port (default: `3306`)
- `DB_NAME`: Your MySQL database name (default: `medicare_db`)
- `SECRET_KEY`: Custom Flask secret key

Alternatively, set the complete connection URL using `DATABASE_URL` environment variable:
```bash
set DATABASE_URL=mysql+pymysql://username:password@host:port/database_name
```



<!-- 

========================================
MEDICONNECT HOSPITAL MANAGEMENT SYSTEM
========================================

PROJECT PATH:
C:\Users\ATHARV RAUT\OneDrive\Desktop\Operations\hospital-management-system


========== KAL WEBSITE RUN KARNE KE STEPS ==========

1. PowerShell kholo

2. Project folder:
cd "C:\Users\ATHARV RAUT\OneDrive\Desktop\Operations\hospital-management-system"

3. Virtual environment:
& "..\.venv\Scripts\Activate.ps1"

4. MySQL settings:
$env:DB_USER="root"
$env:DB_PASSWORD="YOUR_MYSQL_PASSWORD"
$env:DB_HOST="localhost"
$env:DB_PORT="3306"
$env:DB_NAME="mediconnect_db"

5. Flask start:
python run.py

6. Browser:
http://127.0.0.1:5000


========== CURRENT DATABASE ==========

Database:
mediconnect_db

MySQL:
localhost
Port: 3306

IMPORTANT:
schema.sql dobara run NAHI karna.
Existing database/data ko delete NAHI karna.


========== CURRENT LOGIN ACCOUNTS ==========

1. SUPER ADMIN
Role:
SuperAdmin

Email:
admin@mediconnect.com

Password:
admin123


2. HOSPITAL ADMIN
Role:
Hospital Admin

Name:
Rahul Sharma

Email:
admin@mediconnect-demo.com

Password:
Rahul@123

Hospital:
MediConnect Demo Hospital

Registration ID:
MC-DEMO-001


========== HOSPITAL DETAILS ==========

Hospital Name:
MediConnect Demo Hospital

Registration / License Number:
MC-DEMO-001

Hospital Type:
Private

Address:
Pimpri Main Road, Demo Area

State:
Maharashtra

District:
Pune

City:
Pimpri

Website:
https://mediconnect-demo.com

Hospital Email:
admin@mediconnect-demo.com

Hospital Contact:
9876543210


========== IMPORTANT ==========

PowerShell window band mat karna
jab tak website use kar rahe ho.

Server stop karne ke liye:
Ctrl + C

Next day:
upar diye hue steps se sirf server start karna hai.

Database already bana hua hai.
Hospital already registered/approved hai.
Hospital Admin credentials already create kiye hain. -->






<!-- Run Camand start program-> cmd /k ".\start.bat" -->