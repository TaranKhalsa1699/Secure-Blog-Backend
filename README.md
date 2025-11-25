# Secure Blog Backend

A secure Django REST API backend for a blog application, featuring user authentication with JWT, blog CRUD operations, and a fully modular structure. This backend is ready to deploy on platforms like Render.

---

## 🔗 Live Demo

[Secure Blog Backend on Render](https://secure-blog-backend.onrender.com)

---

## 🛠️ Technologies Used

- **Python 3.13**
- **Django 5.2**
- **Django REST Framework**
- **Simple JWT** for authentication
- **PostgreSQL** (via `psycopg2-binary`)
- **Python-dotenv** for environment management

---

## 🚀 Features

- User registration, login, and token refresh endpoints
- Blog CRUD (Create, Read, Update, Delete) operations
- JWT-based authentication for secure endpoints
- Modular app structure: `accounts` & `blog`
- Ready for production deployment (via Gunicorn + Render)

---

## 📦 Installation & Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/TaranKhalsa1699/Secure-Blog-Backend.git
cd Secure-Blog-Backend

2. Create and activate virtual environment
python -m venv venv
Install dependencies

3. Install dependencies
pip install -r requirements.txt

4. Set up environment variables
Create a .env file in the root:

DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DBNAME

5. Apply migrations

python manage.py migrate

6. Run the development server

python manage.py runserver

-->     Visit: http://127.0.0.1:8000

🔑 API Endpoints
Auth

Register: POST /api/auth/register/

Login: POST /api/auth/login/

Refresh token: POST /api/auth/refresh/

Blog (Requires Authentication)

List blogs: GET /api/blog/

Create blog: POST /api/blog/

Retrieve blog: GET /api/blog/<id>/

Update blog: PUT /api/blog/<id>/

Delete blog: DELETE /api/blog/<id>/
