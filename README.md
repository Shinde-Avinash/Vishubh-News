# VishubhNews - News Aggregation Platform

A professional, enterprise-grade News Aggregation Platform built with Django, MySQL, and NewsAPI integration. Features a premium Cognizant-inspired UI design with real-time news updates across multiple categories.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2+-green.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)

## 🌟 Features
<img width="1348" height="597" alt="image" src="https://github.com/user-attachments/assets/fdbbb670-9815-4064-8790-b26496cdb590" />

### Core Functionality
- **Real-time News Aggregation**: Fetches latest news from NewsAPI across 7 categories
- **Category-based Browsing**: Technology, Business, Sports, Health, Science, Entertainment, General
- **Advanced Search**: Search across titles, descriptions, and content
- **Article Bookmarking**: Save favorite articles for later reading
- **User Authentication**: Complete registration, login, and profile management
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices

### Technical Features
- **News Caching**: Articles cached in MySQL for faster performance
- **Auto-refresh**: Intelligent cache refresh mechanism
- **Pagination**: Efficient handling of large article lists
- **Admin Panel**: Full Django admin for content and user management
- **Premium UI/UX**: Cognizant-inspired professional design

## 🎨 Design Philosophy

The UI follows Cognizant's corporate design principles:
- Clean, professional layouts with ample whitespace
- Primary color: Cognizant Blue (#0033A0)
- Modern typography using Inter font
- Card-based design for content organization
- Smooth transitions and minimal animations
- Fully responsive grid system

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- MySQL 8.0 or higher
- pip (Python package manager)
- Git (optional, for version control)

## 🚀 Installation & Setup

### Step 1: Clone or Navigate to Project Directory

```bash
cd "e:/New folder/VishubhCTS/VishubhNews"
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure MySQL Database

1. Open MySQL and create database:
```sql
CREATE DATABASE vishubhnews_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. Create MySQL user (optional but recommended):
```sql
CREATE USER 'newsuser'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON vishubhnews_db.* TO 'newsuser'@'localhost';
FLUSH PRIVILEGES;
```

### Step 5: Configure Environment Variables

1. Copy the example environment file:
```bash
copy .env.example .env
```

2. Edit `.env` file and add your credentials:
```env
SECRET_KEY=your-django-secret-key-here
NEWS_API_KEY=your-newsapi-key-here
DB_NAME=vishubhnews_db
DB_USER=root
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

**Important**: Get your free NewsAPI key from https://newsapi.org/register

### Step 6: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### Step 8: Populate Categories and Fetch News

```bash
python manage.py populate_news
```

This command will:
- Create all 7 news categories
- Fetch latest news from NewsAPI
- Cache articles in the database

### Step 9: Run Development Server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000 in your browser!

## 📱 Application Structure

```
VishubhNews/
├── vishubhnews_project/   # Main project settings
│   ├── settings.py        # Django configuration
│   ├── urls.py           # Root URL configuration
│   └── wsgi.py           # WSGI configuration
├── news/                  # News app
│   ├── models.py         # NewsArticle, Category models
│   ├── views.py          # News listing, detail, search views
│   ├── services.py       # NewsAPI integration
│   ├── admin.py          # Admin configuration
│   └── templates/        # News templates
├── accounts/             # User authentication app
│   ├── models.py        # Extended User model
│   ├── views.py         # Auth views
│   ├── forms.py         # Registration forms
│   └── templates/       # Auth templates
├── bookmarks/           # Bookmarking app
│   ├── models.py       # Bookmark model
│   ├── views.py        # Bookmark views
│   └── templates/      # Bookmark templates
├── static/
│   ├── css/
│   │   └── main.css    # Premium styling
│   └── js/
│       └── main.js     # JavaScript utilities
├── templates/
│   └── base.html       # Base template
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## 🎯 Usage Guide

### For Users

1. **Browse News**: Visit homepage to see latest headlines
2. **Filter by Category**: Click category tabs to filter news
3. **Search**: Use search bar to find specific topics
4. **Read Articles**: Click article cards to view details
5. **Bookmark**: Login and bookmark articles for later
6. **Profile**: Manage your profile and view statistics

### For Administrators

1. Access admin panel: http://127.0.0.1:8000/admin
2. Login with superuser credentials
3. Manage:
   - News articles
   - Categories
   - Users and permissions
   - Bookmarks
   - API usage monitoring

## 🔄 Updating News

### Manual Update
```bash
python manage.py populate_news
```

### Automatic Updates (Production)

For production, set up a cron job or scheduled task to run the populate_news command hourly.

## 🔒 Security Features

- CSRF protection enabled
- SQL injection prevention (Django ORM)
- XSS protection
- Secure password hashing
- Environment-based secrets
- Input validation and sanitization

## 📈 Performance Optimization

- **Database Indexing**: Articles indexed by date and category
- **Query Optimization**: select_related() to reduce queries
- **Caching Strategy**: 1-hour cache refresh interval
- **Pagination**: 20-30 articles per page
- **Image Lazy Loading**: Improved page load times

## 👨‍💻 Developer

Built by Vishubh as a full-stack demonstration project showcasing:
- Django backend development
- MySQL database design
- RESTful API integration
- Corporate UI/UX design
- Enterprise-grade architecture

## 🙏 Acknowledgments

- **NewsAPI.org** for providing news data
- **Cognizant** for design inspiration
- **Django Community** for excellent documentation

---

**Note**: This is a demonstration project. NewsAPI free tier has limitations. For production use, consider upgrading to a paid plan or using alternative news sources.

**Project Status**: ✅ **COMPLETE AND READY TO USE**

Visit the application and start exploring the latest news from around the world! 🌍📰
