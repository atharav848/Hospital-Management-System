@echo off
cd /d "C:\Users\ATHARV RAUT\OneDrive\Desktop\Operations\hospital-management-system"

call "..\.venv\Scripts\activate.bat"

set "DB_USER=root"
set "DB_PASSWORD=JDBCsecure@1"
set "DB_HOST=localhost"
set "DB_PORT=3306"
set "DB_NAME=mediconnect_db"

python run.py

pause