# 🚀 Quick Start - Get Running in 5 Minutes!

## Step 1: Get Your API Key (2 minutes)
1. Go to https://newsapi.org/register
2. Sign up (it's FREE!)
3. Copy your API key
4. Keep it handy for Step 4

## Step 2: Setup Database (1 minute)
Open MySQL and run:
```sql
CREATE DATABASE vishubhnews_db;
```

## Step 3: Run Setup (30 seconds)
```bash
# Windows - just double-click:
setup.bat

# OR run in terminal:
cd "e:/New folder/VishubhCTS/VishubhNews"
setup.bat
```

This will:
- Create your .env file
- Open it in notepad for you to edit

## Step 4: Configure .env File (30 seconds)
In the opened .env file, set these two values:
```env
NEWS_API_KEY=paste-your-key-here
DB_PASSWORD=your-mysql-password
```
Save and close.

## Step 5: Install & Initialize (1 minute)
```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install everything
pip install -r requirements.txt

# Setup database
python manage.py migrate

# Create your admin account (follow prompts)
python manage.py createsuperuser

# Fetch news articles
python manage.py populate_news
```

## Step 6: Launch! (5 seconds)
```bash
python manage.py runserver
```

**Open browser: http://127.0.0.1:8000** 🎉

---

## 🎯 What You Should See

### Homepage
- Latest news headlines in a beautiful grid
- Category tabs (Technology, Sports, Business, etc.)
- Search bar at the top
- Professional blue theme with VishubhNews branding

### Try These Actions:
1. **Browse** - Scroll through news articles
2. **Filter** - Click "Technology" or "Sports" tabs
3. **Search** - Type "AI" or "climate" in search
4. **Sign Up** - Create an account (top right)
5. **Bookmark** - Login and save articles
6. **Admin** - Visit /admin and login with superuser

---

## 🆘 Having Issues?

### MySQL Connection Error
✅ **Fix**: Make sure MySQL is running and password in .env is correct

### No News Showing
✅ **Fix**: Run `python manage.py populate_news`

### API Key Error
✅ **Fix**: Double-check NEWS_API_KEY in .env file

### Import Errors
✅ **Fix**: Activate virtual environment first: `venv\Scripts\activate`

---

## 📚 Next Steps

Once running, check out:
- **README.md** - Full documentation
- **SETUP_GUIDE.md** - Detailed setup guide

---

## 💡 Pro Tips

1. **Refresh News**: Run `python manage.py populate_news` daily
2. **API Limit**: Free tier = 100 requests/day (plenty for testing!)
3. **Admin Panel**: http://127.0.0.1:8000/admin
4. **Responsive**: Try it on mobile, works great!

**Enjoy VishubhNews - Your premium news platform! 📰✨**
