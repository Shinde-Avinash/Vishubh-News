#!/bin/bash

echo "========================================"
echo "News Aggregation Platform - Setup"
echo "========================================"
echo ""

# Check if .env exists
if [ -f .env ]; then
    echo ".env file already exists!"
    echo ""
    read -p "Do you want to overwrite it? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Skipping .env creation..."
    else
        cp .env.example .env
        echo ".env file created!"
    fi
else
    cp .env.example .env
    echo ".env file created successfully!"
fi

echo ""
echo "========================================"
echo "IMPORTANT: Configure your .env file"
echo "========================================"
echo ""
echo "Please edit the .env file and set:"
echo "1. NEWS_API_KEY - Get free key from https://newsapi.org/register"
echo "2. DB_PASSWORD - Your MySQL root password"
echo ""
read -p "Press Enter to open .env file..."
${EDITOR:-nano} .env

echo ""
echo "========================================"
echo "Next Steps:"
echo "========================================"
echo ""
echo "1. Ensure MySQL is running"
echo "2. Create database: CREATE DATABASE news_aggregation_db;"
echo "3. Activate virtual environment: source venv/bin/activate"
echo "4. Install dependencies: pip install -r requirements.txt"
echo "5. Run migrations: python manage.py migrate"
echo "6. Create superuser: python manage.py createsuperuser"
echo "7. Populate news: python manage.py populate_news"
echo "8. Run server: python manage.py runserver"
echo ""
echo "========================================"
echo ""
