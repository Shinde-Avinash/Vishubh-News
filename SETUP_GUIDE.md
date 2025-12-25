# Quick Setup Guide - News Aggregation Platform

## ⚡ Quick Start (5 Minutes)

### 1. Prerequisites Check
- ✅ Python 3.8+ installed
- ✅ MySQL installed and running
- ✅ NewsAPI key (get free at https://newsapi.org/register)

### 2. Environment Setup

```bash
# Navigate to project
cd "e:/New folder/VishubhCTS/news_aggregation"

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Database Setup

Open MySQL and run:
```sql
CREATE DATABASE news_aggregation_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 4. Configure Environment

Edit `.env` file (copy from `.env.example`):
```env
SECRET_KEY=django-insecure-change-this-key
NEWS_API_KEY=YOUR_NEWSAPI_KEY_HERE
DB_NAME=news_aggregation_db
DB_USER=root
DB_PASSWORD=YOUR_MYSQL_PASSWORD
DB_HOST=localhost
DB_PORT=3306
DEBUG=True
```

### 5. Initialize Application

```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Populate categories and fetch news
python manage.py populate_news

# Start server
python manage.py runserver
```

### 6. Access Application

- **Homepage**: http://127.0.0.1:8000
- **Admin Panel**: http://127.0.0.1:8000/admin

## 🎯 First Steps After Setup

1. **Browse News**: Homepage shows latest headlines
2. **Create Account**: Click "Sign Up" to register
3. **Explore Categories**: Use category tabs (Technology, Business, etc.)
4. **Search**: Try searching for topics like "AI", "crypto", "sports"
5. **Bookmark Articles**: Login and bookmark interesting articles
6. **Admin Panel**: Access admin with superuser credentials

## 🔄 Refreshing News

News is automatically cached for 1 hour. To manually refresh:

```bash
python manage.py populate_news
```

## 🎨 Features Overview

### User Features
- ✨ Browse latest news from 30+ sources
- 🏷️ Filter by 7 categories
- 🔍 Search across all articles
- 🔖 Bookmark favorite articles
- 👤 User profile and preferences

### Admin Features
- 📊 View all cached articles
- 👥 Manage users
- 📈 Monitor API usage
- ✏️ Edit/deactivate articles
- 🗂️ Category management

## 💡 Pro Tips

1. **API Limits**: Free NewsAPI allows 100 requests/day. Cache minimizes API calls.
2. **Fresh Content**: Run `populate_news` command daily for latest news.
3. **Responsive Design**: Works perfectly on mobile, tablet, and desktop.
4. **Fast Search**: All articles cached locally for instant search results.

## 🐛 Common Issues

### Issue: Can't connect to database
**Solution**: 
- Ensure MySQL is running
- Check DB credentials in `.env`
- Verify database exists

### Issue: No news displayed
**Solution**: 
```bash
python manage.py populate_news
```

### Issue: NewsAPI error
**Solution**: 
- Verify NEWS_API_KEY in `.env`
- Check daily API limit (100 requests)
- Ensure internet connection

## 📱 Screenshots & Demo

### Homepage
- Clean, professional layout
- Category tabs for easy filtering
- Search bar in header
- Card-based news grid

### Article Detail
- Full article information
- Bookmark functionality
- Related articles
- External link to source

### User Profile
- Account statistics
- Profile management
- Bookmark count
- Member since date

## 🚀 Next Steps

1. **Customize Design**: Edit `static/css/main.css`
2. **Add Categories**: Modify `populate_news.py`
3. **Change API**: Swap NewsAPI with another source
4. **Deploy**: Follow README production guide

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [NewsAPI Docs](https://newsapi.org/docs)
- [MySQL Documentation](https://dev.mysql.com/doc/)

---

**Need Help?** Check the main README.md for detailed troubleshooting and documentation.
