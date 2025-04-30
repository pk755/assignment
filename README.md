# 📝 Assignment 4 – Number Statistics Web Application

## 🎯 Objective

Build a Django web application that allows users to input or upload a list of numbers and returns statistical data such as sum, mean, median, mode, range, prime numbers, and Armstrong numbers. The application also includes a cart system to track unique numbers entered, with a user-friendly UI.

---

## 📌 Features Implemented

- Input field and file upload support for number entry (comma-separated).
- Cart button showing count of unique numbers.
- Results page displaying:
  - ✅ Sum
  - ✅ Mean
  - ✅ Median
  - ✅ Mode
  - ✅ Range
  - ✅ Prime numbers
  - ✅ Armstrong numbers
- Dedicated cart page displaying unique numbers in square containers.
- Clear Cart option.
- Responsive UI with background image and centered, transparent content box.

---

## 🛠 Technologies Used

- Django 5.2
- Python 3.13
- HTML5 & CSS3
- Sessions for cart data

---

## 📁 Folder Structure

```
assignment/
├── assignment/              # Django project settings
├── Statistics/              # Django app
│   ├── static/
│   │   └── Statistics/
│   │       ├── css/
│   │       │   └── styles.css
│   │       └── images/
│   │           └── bgas4-1.png
│   ├── templates/
│   │   └── Statistics/
│   │       ├── homepage.html
│   │       ├── results.html
│   │       └── cart.html
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── ...
├── db.sqlite3
└── manage.py
```

---

## ▶️ How to Run

### 1. Setup Environment
```bash
cd assignment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install django
```

### 2. Run the Server
```bash
python manage.py runserver
```

### 3. Open in Browser
Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📌 Notes

- Input must be a comma-separated list of numbers (e.g., `1,2,3,4`).
- Armstrong logic used: each digit raised to the power of number of digits.
- Cart uses session to store unique numbers.

---

## 🧾 Submission Info

- 🔖 Assignment: 4
- 👨‍🎓 Student: *[Your Name Here]*
- 🏫 Institution: *[Your College/University Name]*
- 🗓️ Date: *[Submission Date]*

---

## 📬 Contact (Optional)

- GitHub: [your-github-url]
- Email: [your-email]
