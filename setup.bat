@echo off
echo ========================================
echo News Aggregation Platform - Setup
echo ========================================
echo.

REM Check if .env exists
if exist .env (
    echo .env file already exists!
    echo.
    choice /C YN /M "Do you want to overwrite it"
    if errorlevel 2 goto skip_env
)

REM Create .env from example
echo Creating .env file...
copy .env.example .env > nul
echo .env file created successfully!
echo.

:skip_env
echo ========================================
echo IMPORTANT: Configure your .env file
echo ========================================
echo.
echo Please edit the .env file and set:
echo 1. NEWS_API_KEY - Get free key from https://newsapi.org/register
echo 2. DB_PASSWORD - Your MySQL root password
echo.
echo Press any key to open .env file in notepad...
pause > nul
notepad .env
echo.

echo ========================================
echo Next Steps:
echo ========================================
echo.
echo 1. Ensure MySQL is running
echo 2. Create database: CREATE DATABASE news_aggregation_db;
echo 3. Activate virtual environment: venv\Scripts\activate
echo 4. Install dependencies: pip install -r requirements.txt
echo 5. Run migrations: python manage.py migrate
echo 6. Create superuser: python manage.py createsuperuser
echo 7. Populate news: python manage.py populate_news
echo 8. Run server: python manage.py runserver
echo.
echo ========================================
echo.
pause
