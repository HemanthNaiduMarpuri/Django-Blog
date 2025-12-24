# 📝 Django Blog Application

A clean and simple blog application built using **Django**, **SQLite**, **HTML**, and **Bootstrap**.  
The project focuses on authentication, role-based access, and a minimal user interface.

---

## 🚀 Features

- 🔐 User authentication (Login & Logout)
- 🧑‍💼 **Only Admin can create and publish blog posts**
- 💬 Authenticated users can add comments
- 🗂 Blog post listing with detail view
- 🎨 Clean and responsive UI using Bootstrap
- 🛡 Secure access control using Django authentication system

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** HTML, Bootstrap
- **Authentication:** Django built-in auth system

---

## 📂 Project Setup

1️⃣ Clone the repository
git clone https://github.com/HemanthNaiduMarpuri/Django-Blog.git
cd Django-Blog
2️⃣ Create and activate virtual environment
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install django

4️⃣ Run migrations
python manage.py migrate

5️⃣ Create superuser (Admin)
python manage.py createsuperuser

6️⃣ Run the server
python manage.py runserver


Open in browser:

http://127.0.0.1:8000/

👤 User Roles
Role	Permissions
Admin	Create, edit, delete blog posts
User	Login and comment on posts
📸 UI Highlights

Minimal and clean layout

Mobile responsive design

Easy navigation

🔮 Future Improvements

Categories & tags

Like system for posts

User profile page

Rich text editor for posts

📄 License

This project is for learning and educational purposes.

🙌 Author

Hemanth Naidu
GitHub: HemanthNaiduMarpuri
