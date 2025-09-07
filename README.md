# 🎨 The Art Agora Backend

This is the **backend service** for **The Art Agora**, built with **Django + Django REST Framework + PostgreSQL**.  
It provides APIs for:

- Artist Onboarding  
- Explorer Subscription  
- Email notifications on submissions
- Agora Store for managing our ecommerce  

---

## 🚀 Features

- Django REST Framework API endpoints  
- PostgreSQL database support  
- Email notifications on new submissions (artists & subscribers)  
- Admin panel for managing data  
- Full Ecommerce with payment integration
- Seeding system for initial product data  

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/the-art-agora-backend.git
cd the-art-agora-backend
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root of the project:

```env
# Database
DATABASE_URL=your-full-public-database-url

# Django
SECRET_KEY=your-secret-key
DEBUG=True

# Email(Locate in backend/settings.py)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password
DEFAULT_FROM_EMAIL=The Art Agora <your_email@gmail.com>
```

⚠️ Replace with your own values.  
For **development only**, you can use Django’s console backend:

```env
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```


### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Seeding data

We’ve added a custom **seed command** to populate initial data (e.g., sample artists, test subscribers).

Run:

If you prefer a Python script:

```bash
python manage.py seed_products
```


---

## 🛠 Running the Server

```bash
python manage.py runserver
```

Visit:

- API Root: `http://127.0.0.1:8000/api/`  
- Admin Panel: `http://127.0.0.1:8000/admin/`  

---

## 📬 Email Testing

If using **console backend** (dev mode), emails will print in your terminal.  

If using **SMTP backend**, test by subscribing:

```bash
curl -X POST http://127.0.0.1:8000/api/subscribe/   -H "Content-Type: application/json"   -d '{"email": "testuser@example.com", "special_requests": "Send me updates!"}'
```

You should receive an email notification at your configured address.

---

## 📌 Endpoints

### Artist Onboarding
- `POST /api/artists/onboarding/` → Submit artist onboarding form

### Explorer Subscribe
- `POST /api/subscribe/` → Submit a subscription

---

## 📖 Development Notes

- Run `python manage.py makemigrations` when models change.  
- Keep `.env` secrets out of version control.  
- Use `EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend` in development.  

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## ✅ Deployment Notes

- Set `DEBUG=False` in `.env` for production  
- Configure `ALLOWED_HOSTS` in `settings.py`  
- Use environment variables for **email + DB credentials**  
- Run `collectstatic` for serving static files  